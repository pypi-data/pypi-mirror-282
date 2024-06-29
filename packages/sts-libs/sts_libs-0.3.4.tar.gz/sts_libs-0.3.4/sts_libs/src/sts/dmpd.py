"""dmpd.py: Module to manipulate LVM thinp and cache metadata devices and snapshot eras."""

#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

import logging
import sys
from pathlib import Path

from sts import linux, lvm
from sts.utils.cli_tools import Wrapper
from sts.utils.cmdline import run, run_ret_out


def _get_devices():  # noqa: ANN202
    return lvm.lv_query()


def _get_active_devices():  # noqa: ANN202
    cmd = 'ls /dev/mapper/'
    retcode, output = run_ret_out(cmd, return_output=True)
    if retcode != 0:
        logging.error('Could not find active dm devices')
        return False
    return output.split()


def _get_device_path(vg_name, lv_name):  # noqa: ANN001, ANN202
    device_path = vg_name + '-' + lv_name
    if '/dev/mapper/' not in device_path:
        device_path = '/dev/mapper/' + device_path
    return device_path


def _check_device(vg_name, lv_name):  # noqa: ANN001, ANN202
    devices = _get_devices()
    device_list = [f['name'] for f in devices]
    if lv_name not in device_list:
        logging.error(f'{lv_name} is not a device')
        return False
    for x in devices:
        if x['name'] == lv_name and x['vg_name'] == vg_name:
            logging.info(f'Found device {lv_name} in group {vg_name}')
            return True
    return False


def _activate_device(vg_name, lv_name):  # noqa: ANN001, ANN202
    devices_active = _get_active_devices()
    if vg_name + '-' + lv_name not in devices_active:
        ret = lvm.lv_activate(lv_name, vg_name)
        if not ret:
            logging.error(f'Could not activate device {lv_name}')
            return False
        logging.info(f'device {lv_name} was activated')
    logging.info(f'device {lv_name} is active')
    return True


def _fallocate(_file, size, command_message):  # noqa: ANN001, ANN202
    cmd = f'fallocate -l {size}M {_file}'
    try:
        retcode = run(cmd).rc
        if retcode != 0:
            logging.error(f'Command failed with code {retcode}.')
            logging.error(f'Could not create file to {command_message} metadata to.')
            return False
    except OSError as e:
        print('command failed: ', e, file=sys.stderr)
        return False
    return True


def get_help(cmd):  # noqa: ANN001, ANN201
    commands = [
        'cache_check',
        'cache_dump',
        'cache_metadata_size',
        'cache_repair',
        'cache_restore',
        'era_check',
        'era_dump',
        'era_invalidate',
        'era_restore',
        'thin_check',
        'thin_delta',
        'thin_dump',
        'thin_ls',
        'thin_metadata_size',
        'thin_repair',
        'thin_restore',
        'thin_rmap',
        'thin_show_duplicates',
        'thin_trim',
    ]
    if cmd not in commands:
        logging.error(f'Unknown command {cmd}')
        return False

    command = f'{cmd} -h'
    retcode = run(command).rc
    if retcode != 0:
        logging.error(f'Could not get help for {cmd}.')
        return False

    return True


def get_version(cmd):  # noqa: ANN001, ANN201
    commands = [
        'cache_check',
        'cache_dump',
        'cache_metadata_size',
        'cache_repair',
        'cache_restore',
        'era_check',
        'era_dump',
        'era_invalidate',
        'era_restore',
        'thin_check',
        'thin_delta',
        'thin_dump',
        'thin_ls',
        'thin_metadata_size',
        'thin_repair',
        'thin_restore',
        'thin_rmap',
        'thin_show_duplicates',
        'thin_trim',
    ]
    if cmd not in commands:
        logging.error(f'Unknown command {cmd}')
        return False

    command = f'{cmd} -V'
    retcode = run(command).rc
    if retcode != 0:
        logging.error(f'Could not get version of {cmd}.')
        return False

    return True


def _get_dev_id(dev_id, path=None, lv_name=None, vg_name=None):  # noqa: ANN001, ANN202
    dev_ids = []

    if path is None:
        retcode, data = thin_dump(source_vg=vg_name, source_lv=lv_name, formatting='xml', return_output=True)
        if not retcode:
            logging.error(f'Could not dump metadata from {vg_name}/{lv_name}')
            return False
        data_lines = data.splitlines()
        for line in data_lines:
            blocks = line.split()
            for block in blocks:
                if not block.startswith('dev_'):
                    continue
                dev_ids.append(int(block[8:-1]))

    else:
        with Path(path, encoding='UTF-8').open() as meta:
            for line in meta:
                blocks = line.split()
                for block in blocks:
                    if not block.startswith('dev_'):
                        continue
                    dev_ids.append(int(block[8:-1]))

    if dev_id in dev_ids:
        return True

    return False


def _metadata_size(source=None, lv_name=None, vg_name=None):  # noqa: ANN001, ANN202
    if source is None:
        cmd = 'lvs -a --units m'
        ret, data = run_ret_out(cmd, return_output=True)
        if ret != 0:
            logging.error('Could not list LVs')
        data_line = data.splitlines()
        for line in data_line:
            cut = line.split()
            if not cut or (lv_name != cut[0] and vg_name != cut[1]):
                continue
            cut = cut[3]
            cut = cut.split('m')
            size = float(cut[0])
            run(cmd)
            return int(size)
        logging.error(f'Could not find {lv_name} {vg_name} in lvs, setting size to 100m')
        return 100
    return int(Path(source).stat().st_size) / 1000000


###########################################
# cache section
###########################################


def cache_check(  # noqa: ANN201
    source_file=None,  # noqa: ANN001
    source_vg=None,  # noqa: ANN001
    source_lv=None,  # noqa: ANN001
    quiet=False,  # noqa: ANN001
    super_block_only=False,  # noqa: ANN001
    clear_needs_check_flag=False,  # noqa: ANN001
    skip_mappings=False,  # noqa: ANN001
    skip_hints=False,  # noqa: ANN001
    skip_discards=False,  # noqa: ANN001
):
    """Check cache pool metadata from either file or device.
    The arguments are:
    source_file
    source_vg VG name
    source_lv LV name
    quiet Mute STDOUT
    super_block_only
    clear_needs_check_flag
    skip_mappings
    skip_hints
    skip_discards
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    options = ''

    if not source_file and (not source_vg or not source_lv):
        logging.error('cache_check requires either source_file OR source_vg and source_lv.')
        return False

    if not source_file:
        ret = _check_device(source_vg, source_lv)
        if not ret:
            return False
        ret = _activate_device(source_vg, source_lv)
        if not ret:
            return False
        device = _get_device_path(source_vg, source_lv)
    else:
        if not Path(source_file).is_file():
            logging.error('Source file is not a file.')
            return False
        device = source_file

    if quiet:
        options += '--quiet '

    if super_block_only:
        options += '--super-block-only '

    if clear_needs_check_flag:
        options += '--clear-needs-check-flag '

    if skip_mappings:
        options += '--skip-mappings '

    if skip_hints:
        options += '--skip-hints '

    if skip_discards:
        options += '--skip-discards '

    cmd = f'cache_check {device} {options}'
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not check {device} metadata')
        return False

    return True


def cache_dump(  # noqa: ANN201
    source_file=None,  # noqa: ANN001
    source_vg=None,  # noqa: ANN001
    source_lv=None,  # noqa: ANN001
    output=None,  # noqa: ANN001
    repair=False,  # noqa: ANN001
    return_output=False,  # noqa: ANN001
):
    """Dumps cache metadata from device of source file to standard output or file.
    The arguments are:
    source_file
    source_vg: VG name
    source_lv: LV name
    output: specify output xml file
    return_output: see 'Returns', not usable with output=True
    repair: Repair the metadata while dumping it
    Returns:
    Only Boolean if return_output False:
    True if success,
    False in case of failure,
    Boolean and data if return_output True.
    """
    options = ''
    data = None

    if return_output and output:
        logging.info('Cannot return to both STDOUT and file, returning only to file.')
        return_output = False

    ret_fail = (False, None) if return_output else False

    if not source_file and (not source_vg or not source_lv):
        logging.error('cache_dump requires either source_file OR source_vg and source_lv.')
        return ret_fail

    if not source_file:
        ret = _check_device(source_vg, source_lv)
        if not ret:
            return ret_fail
        ret = _activate_device(source_vg, source_lv)
        if not ret:
            return ret_fail
        device = _get_device_path(source_vg, source_lv)
    else:
        if not Path(source_file).is_file():
            logging.error('Source file is not a file.')
            return ret_fail
        device = source_file

    if output:
        if not Path(output).is_file():
            size = _metadata_size(source_file, source_lv, source_vg)
            ret = _fallocate(output, size + 1, 'dump')
            if not ret:
                return ret_fail
        options += f'-o {output} '

    if repair:
        options += '--repair'

    cmd = f'cache_dump {device} {options}'
    if return_output:
        retcode, data = run_ret_out(cmd, return_output=True)
    else:
        retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not dump {device} metadata.')
        return ret_fail

    if return_output:
        return True, data
    return True


def cache_repair(  # noqa: ANN201
    source_file=None,  # noqa: ANN001
    source_vg=None,  # noqa: ANN001
    source_lv=None,  # noqa: ANN001
    target_file=None,  # noqa: ANN001
    target_vg=None,  # noqa: ANN001
    target_lv=None,  # noqa: ANN001
):
    """Repairs cache metadata from source file/device to target file/device
    The arguments are:
    source as either source_file OR source_vg and source_lv
    target as either target_file OR target_vg and target_lv
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not source_file and (not source_vg or not source_lv):
        logging.error('cache_repair requires either source_file OR source_vg and source_lv as source.')
        return False

    if not target_file and (not target_vg or not target_lv):
        logging.error('cache_repair requires either target_file OR target_vg and target_lv as target.')
        return False

    if not source_file:
        ret = _check_device(source_vg, source_lv)
        if not ret:
            return False
        ret = _activate_device(source_vg, source_lv)
        if not ret:
            return False
        source = _get_device_path(source_vg, source_lv)
    else:
        if not Path(source_file).is_file():
            logging.error('Source file is not a file.')
            return False
        source = source_file

    if not target_file:
        ret = _check_device(target_vg, target_lv)
        if not ret:
            return False
        ret = _activate_device(target_vg, target_lv)
        if not ret:
            return False
        target = _get_device_path(target_vg, target_lv)
    else:
        if not Path(target_file).is_file():
            size = _metadata_size(source_file, source_lv, source_vg)
            ret = _fallocate(target_file, size + 1, 'repair')
            if not ret:
                return False
        target = target_file

    cmd = f'cache_repair -i {source} -o {target}'
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not repair metadata from {source} to {target}')
        return False

    return True


def cache_restore(  # noqa: ANN201
    source_file,  # noqa: ANN001
    target_vg=None,  # noqa: ANN001
    target_lv=None,  # noqa: ANN001
    target_file=None,  # noqa: ANN001
    quiet=False,  # noqa: ANN001
    metadata_version=None,  # noqa: ANN001
    omit_clean_shutdown=False,  # noqa: ANN001
    override_metadata_version=None,  # noqa: ANN001
):
    """Restores cache metadata from source xml file to target device/file
    The arguments are:
    source_file Source xml file
    target as either target_file OR target_vg and target_lv
    quiet Mute STDOUT
    metadata_version Specify metadata version to restore
    omit_clean_shutdown Disable clean shutdown
    override_metadata_version DEBUG option to override metadata version without checking
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    options = ''

    if source_file is None:
        logging.error('cache_restore requires source file.')
        return False

    if not target_file and (not target_vg or not target_lv):
        logging.error('cache_restore requires either target_file OR target_vg and target_lv as target.')
        return False

    if not Path(source_file).is_file():
        logging.error('Source file is not a file.')
        return False

    if not target_file:
        ret = _check_device(target_vg, target_lv)
        if not ret:
            return False
        ret = _activate_device(target_vg, target_lv)
        if not ret:
            return False
        target = _get_device_path(target_vg, target_lv)
    else:
        if not Path(target_file).is_file():
            size = _metadata_size(source_file)
            ret = _fallocate(target_file, size + 1, 'restore')
            if not ret:
                return False
        target = target_file

    if quiet:
        options += '--quiet '

    if metadata_version:
        options += f'--metadata-version {metadata_version} '

    if omit_clean_shutdown:
        options += '--omit-clean-shutdown '

    if override_metadata_version:
        options += f'--debug-override-metadata-version {override_metadata_version}'

    cmd = f'cache_restore -i {source_file} -o {target} {options}'

    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not restore metadata from {source_file} to {target}')
        return False

    return True


###########################################
# thinp section
###########################################


def thin_check(  # noqa: ANN201
    source_file=None,  # noqa: ANN001
    source_vg=None,  # noqa: ANN001
    source_lv=None,  # noqa: ANN001
    quiet=False,  # noqa: ANN001
    super_block_only=False,  # noqa: ANN001
    clear_needs_check_flag=False,  # noqa: ANN001
    skip_mappings=False,  # noqa: ANN001
    ignore_non_fatal_errors=False,  # noqa: ANN001
):
    """Check thin pool metadata from either file or device.
    The arguments are:
    source_file
    source_vg VG name
    source_lv LV name
    quiet Mute STDOUT
    super_block_only
    clear_needs_check_flag
    skip_mappings
    ignore_non_fatal_errors
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    options = ''

    if not source_file and (not source_vg or not source_lv):
        logging.error('thin_check requires either source_file OR source_vg and source_lv.')
        return False

    if not source_file:
        ret = _check_device(source_vg, source_lv)
        if not ret:
            return False
        ret = _activate_device(source_vg, source_lv)
        if not ret:
            return False
        device = _get_device_path(source_vg, source_lv)
    else:
        if not Path(source_file).is_file():
            logging.error('Source file is not a file.')
            return False
        device = source_file

    if quiet:
        options += '--quiet '

    if super_block_only:
        options += '--super-block-only '

    if clear_needs_check_flag:
        options += '--clear-needs-check-flag '

    if skip_mappings:
        options += '--skip-mappings '

    if ignore_non_fatal_errors:
        options += '--ignore-non-fatal-errors '

    cmd = f'thin_check {device} {options}'
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not check {device} metadata')
        return False

    return True


def thin_ls(source_vg, source_lv, no_headers=False, fields=None, snapshot=False):  # noqa: ANN001, ANN201
    """List information about thin LVs on thin pool.
    The arguments are:
    source_vg VG name
    source_lv LV name
    fields list of fields to output, default is all
    snapshot Use metadata snapshot, able to run on live snapshotted pool
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    options = ''

    if not source_vg or not source_lv:
        logging.error('thin_ls requires source_vg and source_lv.')
        return False

    ret = _check_device(source_vg, source_lv)
    if not ret:
        return False
    ret = _activate_device(source_vg, source_lv)
    if not ret:
        return False
    device = _get_device_path(source_vg, source_lv)

    if no_headers:
        options += '--no-headers '

    fields_possible = [
        'DEV',
        'MAPPED_BLOCKS',
        'EXCLUSIVE_BLOCKS',
        'SHARED_BLOCKS',
        'MAPPED_SECTORS',
        'EXCLUSIVE_SECTORS',
        'SHARED_SECTORS',
        'MAPPED_BYTES',
        'EXCLUSIVE_BYTES',
        'SHARED_BYTES',
        'MAPPED',
        'EXCLUSIVE',
        'TRANSACTION',
        'CREATE_TIME',
        'SHARED',
        'SNAP_TIME',
    ]
    if fields is None:
        options += f" --format \"{','.join([str(i) for i in fields_possible])}\" "
    else:
        for field in fields:
            if field not in fields_possible:
                logging.error(f'Unknown field {field} specified.')
                logging.info(f"Possible fields are: {', '.join([str(i) for i in fields_possible])}")
                return False
        options += f" --format \"{','.join([str(i) for i in fields])}\" "

    if snapshot:
        options += '--metadata-snap'

    cmd = f'thin_ls {device} {options}'
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not list {device} metadata')
        return False

    return True


def thin_dump(  # noqa: ANN201
    source_file=None,  # noqa: ANN001
    source_vg=None,  # noqa: ANN001
    source_lv=None,  # noqa: ANN001
    output=None,  # noqa: ANN001
    repair=False,  # noqa: ANN001
    formatting=None,  # noqa: ANN001
    snapshot=None,  # noqa: ANN001
    dev_id=None,  # noqa: ANN001
    skip_mappings=False,  # noqa: ANN001
    return_output=False,  # noqa: ANN001
):
    """Dumps thin metadata from device of source file to standard output or file.
    The arguments are:
    source_file
    source_vg: VG name
    source_lv: LV name
    output: specify output xml file
    return_output: see 'Returns', not usable with output=True
    repair: Repair the metadata while dumping it
    formatting: Specify output format [xml, human_readable, custom='file']
    snapshot: (Boolean/Int) Use metadata snapshot. If Int provided, specifies block number
    dev_id: id of the device
    Returns:
    Only Boolean if return_output False:
    True if success
    False in case of failure
    Boolean and data if return_output True.
    """
    options = ''
    data = None

    if return_output and output:
        logging.info('Cannot return to both STDOUT and file, returning only to file.')
        return_output = False

    ret_fail = (False, None) if return_output else False

    if not source_file and (not source_vg or not source_lv):
        logging.error('thin_dump requires either source_file OR source_vg and source_lv.')
        return ret_fail

    if not source_file:
        ret = _check_device(source_vg, source_lv)
        if not ret:
            return ret_fail
        ret = _activate_device(source_vg, source_lv)
        if not ret:
            return ret_fail
        device = _get_device_path(source_vg, source_lv)
    else:
        if not Path(source_file).is_file():
            logging.error('Source file is not a file.')
            return ret_fail
        device = source_file

    if output:
        if not Path(output).is_file():
            size = _metadata_size(source_file, source_lv, source_vg)
            ret = _fallocate(output, size + 1, 'dump')
            if not ret:
                return ret_fail
        options += f'-o {output} '

    if repair:
        options += '--repair '

    if snapshot:
        if isinstance(snapshot, bool):
            options += '--metadata-snap '
        elif isinstance(snapshot, int):
            options += f'--metadata-snap {snapshot} '
        else:
            logging.error('Unknown snapshot value, use either Boolean or Int.')
            return ret_fail

    if formatting:
        if formatting in {'xml', 'human_readable'}:
            options += f'--format {formatting} '
        elif formatting.startswith('custom='):
            if not Path(formatting[8:-1]).is_file():
                logging.error('Specified custom formatting file is not a file.')
                return ret_fail
            options += f'--format {formatting} '
        else:
            logging.error("Unknown formatting specified, please use one of [xml, human_readable, custom='file'].")
            return ret_fail

    if dev_id:
        if isinstance(dev_id, int):
            if _get_dev_id(dev_id, source_file, source_lv, source_vg):
                options += f'--dev-id {dev_id} '
            else:
                logging.error(f'Unknown dev_id value, device with id {dev_id} does not exist.')
                return ret_fail
        else:
            logging.error('Unknown dev_id value, must be Int.')
            return ret_fail

    if skip_mappings:
        options += '--skip-mappings '

    cmd = f'thin_dump {device} {options}'
    if return_output:
        retcode, data = run_ret_out(cmd, return_output=True)
    else:
        retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not dump {device} metadata.')
        return ret_fail

    if return_output:
        return True, data
    return True


def thin_restore(  # noqa: ANN201
    source_file,  # noqa: ANN001
    target_vg=None,  # noqa: ANN001
    target_lv=None,  # noqa: ANN001
    target_file=None,  # noqa: ANN001
    quiet=False,  # noqa: ANN001
):
    """Restores thin metadata from source xml file to target device/file
    The arguments are:
    source_file Source xml file
    target as either target_file OR target_vg and target_lv
    quiet Mute STDOUT
    metadata_version Specify metadata version to restore
    omit_clean_shutdown Disable clean shutdown
    override_metadata_version DEBUG option to override metadata version without checking
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    options = ''

    if source_file is None:
        logging.error('thin_restore requires source file.')
        return False

    if not target_file and (not target_vg or not target_lv):
        logging.error('thin_restore requires either target_file OR target_vg and target_lv as target.')
        return False

    if not Path(source_file).is_file():
        logging.error('Source file is not a file.')
        return False

    if not target_file:
        ret = _check_device(target_vg, target_lv)
        if not ret:
            return False
        ret = _activate_device(target_vg, target_lv)
        if not ret:
            return False
        target = _get_device_path(target_vg, target_lv)
    else:
        if not Path(target_file).is_file():
            size = _metadata_size(source_file)
            ret = _fallocate(target_file, size + 1, 'restore')
            if not ret:
                return False
        target = target_file

    if quiet:
        options += '--quiet'

    cmd = f'thin_restore -i {source_file} -o {target} {options}'

    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not restore metadata from {source_file} to {target}')
        return False

    return True


def thin_repair(  # noqa: ANN201
    source_file=None,  # noqa: ANN001
    source_vg=None,  # noqa: ANN001
    source_lv=None,  # noqa: ANN001
    target_file=None,  # noqa: ANN001
    target_vg=None,  # noqa: ANN001
    target_lv=None,  # noqa: ANN001
):
    """Repairs thin metadata from source file/device to target file/device
    The arguments are:
    source as either source_file OR source_vg and source_lv
    target as either target_file OR target_vg and target_lv
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not source_file and (not source_vg or not source_lv):
        logging.error('thin_repair requires either source_file OR source_vg and source_lv as source.')
        return False

    if not target_file and (not target_vg or not target_lv):
        logging.error('thin_repair requires either target_file OR target_vg and target_lv as target.')
        return False

    if not source_file:
        ret = _check_device(source_vg, source_lv)
        if not ret:
            return False
        ret = _activate_device(source_vg, source_lv)
        if not ret:
            return False
        source = _get_device_path(source_vg, source_lv)
    else:
        if not Path(source_file).is_file():
            logging.error('Source file is not a file.')
            return False
        source = source_file

    if not target_file:
        ret = _check_device(target_vg, target_lv)
        if not ret:
            return False
        ret = _activate_device(target_vg, target_lv)
        if not ret:
            return False
        target = _get_device_path(target_vg, target_lv)
    else:
        if not Path(target_file).is_file():
            size = _metadata_size(source_file, source_lv, source_vg)
            ret = _fallocate(target_file, size + 1, 'repair')
            if not ret:
                return False
        target = target_file

    cmd = f'thin_repair -i {source} -o {target}'
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not repair metadata from {source} to {target}')
        return False

    return True


def thin_rmap(region, source_file=None, source_vg=None, source_lv=None):  # noqa: ANN001, ANN201
    """Output reverse map of a thin provisioned region of blocks from metadata device.
    The arguments are:
    source_vg VG name
    source_lv LV name
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not source_file and (not source_vg or not source_lv):
        logging.error('thin_rmap requires either source_file OR source_vg and source_lv as source.')
        return False

    if not source_file:
        ret = _check_device(source_vg, source_lv)
        if not ret:
            return False
        ret = _activate_device(source_vg, source_lv)
        if not ret:
            return False
        device = _get_device_path(source_vg, source_lv)
    else:
        if not Path(source_file).is_file():
            logging.error('Source file is not a file.')
            return False
        device = source_file

    regions = region.split('.')
    try:
        int(regions[0])
        if regions[1]:
            raise ValueError  # noqa: TRY301
        int(regions[2])
        if regions[3] is not None:
            raise ValueError  # noqa: TRY301
    except ValueError:
        logging.exception("Region must be in format 'INT..INT'")
        return False
    except IndexError:
        pass
    # region 1..-1 must be valid, using unsigned 32bit ints
    if int(regions[0]) & 0xFFFFFFFF >= int(regions[2]) & 0xFFFFFFFF:
        logging.error('Beginning of the region must be before its end.')
        return False
    options = f'--region {region}'

    cmd = f'thin_rmap {device} {options}'
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not output reverse map from {device} metadata device')
        return False

    return True


def thin_trim(  # noqa: ANN201
    data_vg,  # noqa: ANN001
    data_lv,  # noqa: ANN001
    metadata_vg=None,  # noqa: ANN001
    metadata_lv=None,  # noqa: ANN001
    metadata_file=None,  # noqa: ANN001
):
    """Issue discard requests for free pool space.
    The arguments are:
    data_vg VG name of data device
    data_lv LV name of data device
    metadata_vg VG name of metadata device
    metadata_lv LV name of metadata device
    metadata_file file with metadata
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    options = ''

    if not data_vg or not data_lv:
        logging.error('thin_trim requires data_vg and data_lv.')
        return False

    if not metadata_file and (not metadata_vg or not metadata_lv):
        logging.error('thin_trim requires either metadata_file OR metadata_vg and metadata_lv as target.')
        return False

    ret = _check_device(data_vg, data_lv)
    if not ret:
        return False

    ret = _activate_device(data_vg, data_lv)
    if not ret:
        return False

    if not metadata_file:
        ret = _check_device(metadata_vg, metadata_lv)
        if not ret:
            return False
        ret = _activate_device(metadata_vg, metadata_lv)
        if not ret:
            return False
        metadata_dev = _get_device_path(metadata_vg, metadata_lv)
    else:
        if not Path(metadata_file).is_file():
            logging.error(f'metadata_file {metadata_file} is not a file.')
            return False
        metadata_dev = metadata_file

    data_dev = _get_device_path(data_vg, data_lv)
    cmd = f'thin_trim --data-dev {data_dev} --metadata-dev {metadata_dev} {options}'
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not discard free pool space on device {data_dev} with metadata device {metadata_dev}.')
        return False

    return True


def thin_delta(  # noqa: ANN201
    thin1,  # noqa: ANN001
    thin2,  # noqa: ANN001
    source_file=None,  # noqa: ANN001
    source_vg=None,  # noqa: ANN001
    source_lv=None,  # noqa: ANN001
    snapshot=False,  # noqa: ANN001
    verbosity=False,  # noqa: ANN001
):
    """Print the differences in the mappings between two thin devices.
    The arguments are:
    source_vg VG name
    source_lv LV name
    thin1 numeric identificator of first thin volume
    thin2 numeric identificator of second thin volume
    snapshot (Boolean/Int) Use metadata snapshot. If Int provided, specifies block number
    verbosity Provide extra information on the mappings
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    options = ''

    if not source_file and (not source_vg or not source_lv):
        logging.error('thin_delta requires either source_file OR source_vg and source_lv.')
        return False

    if not source_file:
        ret = _check_device(source_vg, source_lv)
        if not ret:
            return False
        ret = _activate_device(source_vg, source_lv)
        if not ret:
            return False
        device = _get_device_path(source_vg, source_lv)
    else:
        if not Path(source_file).is_file():
            logging.error('Source file is not a file.')
            return False
        device = source_file

    if snapshot:
        if isinstance(snapshot, bool):
            options += '--metadata-snap '
        elif isinstance(snapshot, int):
            options += f'--metadata-snap {snapshot} '
        else:
            logging.error('Unknown snapshot value, use either Boolean or Int.')
            return False

    if verbosity:
        options += '--verbose'

    if _get_dev_id(thin1, source_file, source_lv, source_vg) and _get_dev_id(thin2, source_file, source_lv, source_vg):
        cmd = f'thin_delta {options} --thin1 {thin1} --thin2 {thin2} {device}'
        retcode = run(cmd).rc
        if retcode != 0:
            logging.error('Could not get differences in mappings between two thin LVs.')
            return False
    else:
        logging.error('Specified id does not exist.')
        return False
    return True


class DMPD(Wrapper):
    def __init__(self, disable_check=True) -> None:  # noqa: ANN001
        self.disable_check = disable_check

        pkg = 'device-mapper-persistent-data'
        if not linux.is_installed(pkg) and not linux.install_package(pkg):
            logging.critical(f'Could not install {pkg} package')

        self.commands: dict[str, str | list[str]] = {
            'cache_check': 'cache_check',
            'cache_dump': 'cache_dump',
            'cache_metadata_size': 'cache_metadata_size',
            'cache_repair': 'cache_repair',
            'cache_restore': 'cache_restore',
            'cache_writeback': 'cache_writeback',
            'thin_check': 'thin_check',
            'thin_delta': 'thin_delta',
            'thin_dump': 'thin_dump',
            'thin_ls': 'thin_ls',
            'thin_metadata_size': 'thin_metadata_size',
            'thin_repair': 'thin_repair',
            'thin_restore': 'thin_restore',
            'thin_rmap': 'thin_rmap',
            'thin_trim': 'thin_trim',
        }
        self.commands['all'] = list(self.commands.keys())
        self.arguments = {
            'help': [self.commands['all'], ' --help'],
            'version': [self.commands['all'], ' --version'],
            'verbose': [self.commands['all'], ' --verbose'],
            'block_size': [
                ['cache_metadata_size', 'thin_metadata_size'],
                ' --block-size&',
            ],
            'buffer_size': [['cache_writeback'], ' --buffer-size-meg&'],
            'clear_needs_check_flag': [
                ['cache_check', 'thin_check'],
                ' --clear-needs-check-flag',
            ],
            'data_dev': [['thin_trim'], ' --data-dev&'],
            'debug_override_metadata_version': [
                ['cache_restore'],
                ' --debug-override-metadata-version&',
            ],
            'dev_id': [['thin_dump'], ' --dev-id&'],
            'device_size': [['cache_metadata_size'], ' --device-size&'],
            'fast_device': [['cache_writeback'], ' --fast-device&'],
            'format': [['thin_ls', 'thin_dump'], ' --format&'],
            'ignore_non_fatal_errors': [['thin_check'], ' --ignore-non-fatal-errors'],
            'input': [
                ['cache_repair', 'cache_restore', 'thin_repair', 'thin_restore'],
                ' -i&',
            ],
            'list_failed_blocks': [['cache_writeback'], ' --list-failed-blocks'],
            'max_hint_width': [['cache_metadata_size'], ' --max-hint-width&'],
            'max_thins': [['thin_metadata_size'], ' --max-thins&'],
            'metadata_dev': [['thin_trim'], ' --metadata-dev&'],
            'metadata_device': [['cache_writeback'], ' --metadata-device&'],
            'metadata_snap': [['thin_dump', 'thin_delta'], ' --metadata-snap&'],
            'metadata_version': [['cache_restore'], ' --metadata-version&'],
            'no_headers': [['thin_ls'], ' --no-headers'],
            'no_metadata_update': [['cache_writeback'], ' --no-metadata-update'],
            'nr_blocks': [['cache_metadata_size'], ' --nr-blocks&'],
            'numeric_only': [['thin_metadata_size'], ' --numeric-only'],
            'numeric_only_type': [['thin_metadata_size'], ' --numeric-only='],
            'omit_clean_shutdown': [['cache_restore'], ' --omit-clean-shutdown'],
            'origin_device': [['cache_writeback'], ' --origin-device&'],
            'output': [
                [
                    'cache_dump',
                    'cache_repair',
                    'cache_restore',
                    'thin_dump',
                    'thin_repair',
                    'thin_restore',
                ],
                ' -o&',
            ],
            'override_mapping_root': [['thin_check'], ' --override-mapping-root&'],
            'pool_size': [['thin_metadata_size'], ' --pool-size&'],
            'quiet': [
                ['cache_check', 'cache_restore', 'thin_check', 'thin_restore'],
                ' --quiet',
            ],
            'region': [['thin_rmap'], ' --region&'],
            'repair': [['cache_dump', 'thin_dump'], ' --repair'],
            'skip_discards': [['cache_check'], ' --skip-discards'],
            'skip_hints': [['cache_check'], ' --skip-hints'],
            'skip_mappings': [['thin_check', 'thin_dump'], ' --skip-mappings'],
            'snap1': [['thin_delta'], ' --snap1&'],
            'snap2': [['thin_delta'], ' --snap2&'],
            'snapshot': [['thin_ls', 'thin_dump', 'thin_delta'], ' --metadata-snap'],
            'super_block_only': [['cache_check', 'thin_check'], ' --super-block-only'],
            'thin1': [['thin_delta'], ' --thin1&'],
            'thin2': [['thin_delta'], ' --thin2&'],
            'unit': [['thin_metadata_size'], ' --unit&'],
        }

        Wrapper.__init__(self, self.commands, self.arguments, self.disable_check)

    @staticmethod
    def _remove_nones(kwargs):  # noqa: ANN001, ANN205
        return {k: v for k, v in kwargs.items() if v is not None}

    def _get_possible_arguments(self, command=None):  # noqa: ANN001, ANN202
        return super()._get_possible_arguments(command.split()[0])

    def _run(self, cmd, **kwargs):  # noqa: ANN001, ANN003, ANN202
        # Constructs the command to run and runs it
        cmd = self._add_arguments(cmd, **kwargs)

        ret = run(cmd).rc
        if isinstance(ret, tuple) and ret[0] != 0:
            logging.warning(f"Running command: '{cmd}' failed. Return with output.")
        elif isinstance(ret, int) and ret != 0:
            logging.warning(f"Running command: '{cmd}' failed.")
        return ret

    def cache_check(self, source_file=None, source_vg=None, source_lv=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'cache_check '
        if source_file:
            cmd += f'{source_file} '
        if source_vg and source_lv:
            cmd += f'{_get_device_path(source_vg, source_lv)} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def cache_dump(self, source_file=None, source_vg=None, source_lv=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'cache_dump '
        if source_file:
            cmd += f'{source_file} '
        if source_vg and source_lv:
            cmd += f'{_get_device_path(source_vg, source_lv)} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def cache_metadata_size(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'cache_metadata_size '
        return self._run(cmd, **self._remove_nones(kwargs))

    def cache_repair(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'cache_repair '
        return self._run(cmd, **self._remove_nones(kwargs))

    def cache_restore(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'cache_restore '
        return self._run(cmd, **self._remove_nones(kwargs))

    def cache_writeback(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'cache_writeback '
        return self._run(cmd, **self._remove_nones(kwargs))

    def thin_check(self, source_file=None, source_vg=None, source_lv=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'thin_check '
        if source_file:
            cmd += f'{source_file} '
        if source_vg and source_lv:
            cmd += f'{_get_device_path(source_vg, source_lv)} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def thin_delta(self, source_file=None, source_vg=None, source_lv=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'thin_delta '
        if source_file:
            cmd += f'{source_file} '
        if source_vg and source_lv:
            cmd += f'{_get_device_path(source_vg, source_lv)} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def thin_dump(self, source_file=None, source_vg=None, source_lv=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'thin_dump '
        if source_file:
            cmd += f'{source_file} '
        if source_vg and source_lv:
            cmd += f'{_get_device_path(source_vg, source_lv)} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def thin_ls(self, source_vg=None, source_lv=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'thin_ls '
        if source_vg and source_lv:
            cmd += _get_device_path(source_vg, source_lv)
        return self._run(cmd, **self._remove_nones(kwargs))

    def thin_metadata_size(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'thin_metadata_size '
        return self._run(cmd, **self._remove_nones(kwargs))

    def thin_repair(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'thin_repair '
        return self._run(cmd, **self._remove_nones(kwargs))

    def thin_restore(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'thin_restore '
        return self._run(cmd, **self._remove_nones(kwargs))

    def thin_rmap(self, source_file=None, source_vg=None, source_lv=None, **kwargs):  # noqa: ANN001, ANN003, ANN201
        cmd = 'thin_rmap '
        if source_file:
            cmd += f'{source_file} '
        if source_vg and source_lv:
            cmd += f'{_get_device_path(source_vg, source_lv)} '
        return self._run(cmd, **self._remove_nones(kwargs))

    def thin_trim(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'thin_trim '
        return self._run(cmd, **self._remove_nones(kwargs))
