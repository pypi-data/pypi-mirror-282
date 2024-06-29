"""lvm.py: Module with test specific method for LVM."""

#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import annotations

import fileinput
import logging
import re
from functools import wraps
from pathlib import Path

from sts import vdo
from sts.utils.cli_tools import Wrapper
from sts.utils.cmdline import run, run_ret_out


def check_lv_expected_value(test_obj, lv_name, vg_name, opt_val_dict):  # noqa: ANN001, ANN201
    if not test_obj or not opt_val_dict or not lv_name or not vg_name:
        return

    opt_str = ','.join(opt_val_dict)
    lv = lv_info(lv_name, vg_name, options=opt_str)
    if not lv:
        test_obj.tfail(f'{vg_name}/{lv_name} does not exist')
        run(f'lvs -a -o +{opt_str}')
        return
    for opt in opt_val_dict:
        if lv[opt] == opt_val_dict[opt]:
            test_obj.tpass(f'{vg_name}/{lv_name} {opt} == {opt_val_dict[opt]}')
            continue

        if test_obj.tfail(f'{vg_name}/{lv_name} {opt} == {lv[opt]}, but expected {opt_val_dict[opt]}'):
            print(lv)
            run(f'lvs -a -o +{opt_str}')
            continue


###########################################
# PV section
###########################################
def pv_query():  # noqa: ANN201
    """Query Physical Volumes and return a dictionary with PV information for each PV.
    The arguments are:
    None
    Returns:
    dict: Return a dictionary with PV info for each PV.
    """
    cmd = 'pvs --noheadings --separator ","'
    retcode, output = run_ret_out(cmd, return_output=True)
    if retcode != 0:
        logging.debug('there are no VGs')
        return None
    pvs = output.split('\n')

    # format of PV info: PV,VG,Fmt,Attr,PSize,PFree
    pv_info_regex = r'\s+(\S+),(\S+)?,(\S+),(.*),(.*),(.*)$'

    pv_dict = {}
    for pv in pvs:
        m = re.match(pv_info_regex, pv)
        if not m:
            # logging.warning("(%s) does not match vgdisplay output format" % vg)
            continue
        pv_info_dict = {
            'vg': m.group(2),
            'fmt': m.group(3),  # not sure what it is
            'attr': m.group(4),
            'psize': m.group(5),
            'pfree': m.group(6),
        }
        pv_dict[m.group(1)] = pv_info_dict

    return pv_dict


def pv_create(pv_name: str, options=''):  # noqa: ANN001, ANN201
    """Create a Volume Group.
    The arguments are:
    PV name
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not pv_name:
        logging.error('pv_create requires pv_name')
        return False
    cmd = f'pvcreate {options} {pv_name}'
    if run(cmd).rc != 0:
        # print ("FAIL: Could not create %s" % pv_name)
        return False
    return True


def pv_remove(pv_name: str, force=None) -> bool:  # noqa: ANN001
    """Delete a Volume Group.
    The arguments are:
    VG name
    force (boolean)
    verbose (boolean).

    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not pv_name:
        logging.error('pv_remove requires pv_name')
        return False

    pv_dict = pv_query()

    pv_names = pv_name.split()
    for name in pv_names:
        if name not in list(pv_dict.keys()):
            logging.info(f'pv_remove - {name} does not exist. Skipping...')
            return True

        options = ''
        if force:
            options += '--force --force'
        cmd = f'pvremove {options} {pv_name}'
        retcode = run(cmd).rc
        if retcode != 0:
            logging.error(f'Could not delete {pv_name}')
            return False
    return True


###########################################
# VG section
###########################################


def vg_show():  # noqa: ANN201
    """Show information for Volume Groups
    The arguments are:
    None
    Returns:
    True
    or
    False.
    """
    cmd = 'vgs -a'
    if run(cmd).rc != 0:
        logging.error('Could not show VGs')
        return False
    return True


def vg_query():  # noqa: ANN201
    """Query Volume Groups and return a dictonary with VG information for each VG.
    The arguments are:
    None
    Returns:
    dict: Return a dictionary with VG info for each VG.
    """
    cmd = 'vgs --noheadings --separator ","'
    retcode, output = run_ret_out(cmd, return_output=True)
    if retcode != 0:
        logging.debug('there are no VGs')
        return None
    vgs = output.split('\n')

    # format of VG info: name #PV #LV #SN Attr VSize VFree
    vg_info_regex = r'\s+(\S+),(\S+),(\S+),(.*),(.*),(.*),(.*)$'

    vg_dict = {}
    for vg in vgs:
        m = re.match(vg_info_regex, vg)
        if not m:
            # logging.warning("(%s) does not match vgdisplay output format" % vg)
            continue
        vg_info_dict = {
            'num_pvs': m.group(2),
            'num_lvs': m.group(3),
            'num_sn': m.group(4),  # not sure what it is
            'attr': m.group(5),
            'vsize': m.group(6),
            'vfree': m.group(7),
        }
        vg_dict[m.group(1)] = vg_info_dict

    return vg_dict


def vg_create(vg_name: str, pv_name: str, force=False):  # noqa: ANN001, ANN201
    """Create a Volume Group.
    The arguments are:
    PV name
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not vg_name or not pv_name:
        logging.error('vg_create requires vg_name and pv_name')
        return False

    options = ''
    if force:
        options += '--force'
    cmd = f'vgcreate {options} {vg_name} {pv_name}'
    retcode = run(cmd).rc
    if retcode != 0:
        # print ("FAIL: Could not create %s" % vg_name)
        return False
    return True


def vg_remove(vg_name: str, force=False):  # noqa: ANN001, ANN201
    """Delete a Volume Group.
    The arguments are:
    VG name
    force (boolean).

    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not vg_name:
        logging.error('vg_remove requires vg_name')
        return False

    vg_dict = vg_query()
    if vg_name not in list(vg_dict.keys()):
        logging.info(f'vg_remove - {vg_name} does not exist. Skipping...')
        return True

    options = ''
    if force:
        options += '--force'
    cmd = f'vgremove {options} {vg_name}'
    retcode = run(cmd).rc
    if retcode != 0:
        # print ("FAIL: Could not delete %s" % vg_name)
        return False
    return True


###########################################
# LV section
###########################################


def lv_show():  # noqa: ANN201
    """Show information for Logical Volumes
    The arguments are:
    None
    Returns:
    True
    or
    False.
    """
    cmd = 'lvs -a'
    if run(cmd).rc != 0:
        logging.error('Could not show LVs')
        return False
    return True


def lv_query(options=''):  # noqa: ANN001, ANN201
    """Query Logical Volumes and return a dictonary with LV information for each LV.
    The arguments are:
    options:  If not want to use default lvs output. Use -o for no default fields
    Returns:
    dict: Return a list with LV info for each LV.
    """
    # Use \",\" as separator, as some output might contain ','
    # For example, lvs -o modules on thin device returns "thin,thin-pool"
    cmd = 'lvs -a --noheadings --separator \\",\\"'

    # format of LV info: Name VG Attr LSize Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
    lv_info_regex = (
        r'\s+(\S+)\",\"(\S+)\",\"(\S+)\"'
        r',\"(\S+)\",\"(.*)\",\"(.*)\",\"(.*)\",\"(.*)\",\"(.*)\",\"(.*)\",\"(.*)\",\"(.*)$'
    )

    # default parameters returned by lvs -a
    param_names = [
        'name',
        'vg_name',
        'attr',
        'size',
        'pool',
        'origin',
        'data_per',
        'meta_per',
        'move',
        'log',
        'copy_per',
        'convert',
    ]

    if options:
        param_names = ['name', 'vg_name']
        # need to change default regex
        lv_info_regex = r'\s+(\S+)\",\"(\S+)'
        parameters = options.split(',')
        for param in parameters:
            lv_info_regex += '","(.*)'
            param_names.append(param)
        lv_info_regex += '$'
        cmd += f' -o lv_name,vg_name,{options}'

    retcode, output = run_ret_out(cmd, return_output=True)
    if retcode != 0:
        logging.debug('there are no LVs')
        return None
    lvs = output.split('\n')

    lv_list = []
    for lv in lvs:
        m = re.match(lv_info_regex, lv)
        if not m:
            logging.error(f'({lv}) does not match lvs output format')
            continue
        lv_info_dict = {}
        for index in range(len(param_names)):
            lv_info_dict[param_names[index]] = m.group(index + 1)
        lv_list.append(lv_info_dict)

    return lv_list


def lv_create(vg_name: str, lv_name: str, options: list):  # noqa: ANN201
    """Create a Logical Volume.
    The arguments are:
    VG name
    LV name
    options
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not vg_name or not lv_name:
        logging.error('lv_create requires vg_name and lv_name')
        return False

    cmd = f"lvcreate {' '.join(str(i) for i in options)} {vg_name} -n {lv_name}"
    retcode = run(cmd).rc
    if retcode != 0:
        # print ("FAIL: Could not create %s" % lv_name)
        return False
    return True


def lv_info(lv_name: str, vg_name: str, options=''):  # noqa: ANN001, ANN201
    """Show information of specific LV."""
    if not lv_name or not vg_name:
        logging.error('lv_info() - requires lv_name and vg_name as parameters')
        return None

    lvs = lv_query(options=options)

    if not lvs:
        return None

    for lv in lvs:
        if lv['name'] == lv_name and lv['vg_name'] == vg_name:
            return lv
    return None


def lv_activate(lv_name: str, vg_name: str):  # noqa: ANN201
    """Activate a Logical Volume
    The arguments are:
    LV name
    VG name
    Returns:
    Boolean:
    True in case of success
    False if something went wrong.
    """
    if not lv_name or not vg_name:
        logging.error('lv_activate requires lv_name and vg_name')
        return False

    cmd = f'lvchange -ay {vg_name}/{lv_name}'
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not activate LV {lv_name}')
        return False

    # Maybe we should query the LVs and make sure it is really activated
    return True


def lv_deactivate(lv_name: str, vg_name: str):  # noqa: ANN201
    """Deactivate a Logical Volume
    The arguments are:
    LV name
    VG name
    Returns:
    Boolean:
    True in case of success
    False if something went wrong.
    """
    if not lv_name or not vg_name:
        logging.error('lv_deactivate requires lv_name and vg_name')
        return False

    cmd = f'lvchange -an {vg_name}/{lv_name}'
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not deactivate LV {lv_name}')
        return False

    # Maybe we should query the LVs and make sure it is really deactivated
    return True


def lv_remove(lv_name: str, vg_name: str):  # noqa: ANN201
    """Remove an LV from a VG
    The arguments are:
    LV name
    VG name
    Returns:
    Boolean:
    True in case of success
    False if something went wrong.
    """
    if not lv_name or not vg_name:
        logging.error('lv_remove requires lv_name and vg_name')
        return False

    lv_names = lv_name.split()

    for name in lv_names:
        if not lv_info(name, vg_name):
            logging.info(f'lv_remove - LV {name} does not exist. Skipping')
            continue

        cmd = f'lvremove --force {vg_name}/{lv_name}'
        retcode = run(cmd).rc
        if retcode != 0:
            logging.error(f'Could not remove LV {lv_name}')
            return False

        if lv_info(lv_name, vg_name):
            logging.info(f'lv_remove - LV {lv_name} still exists.')
            return False

    return True


def lv_convert(vg_name: str, lv_name: str, options: list):  # noqa: ANN201
    """Change Logical Volume layout.
    The arguments are:
    VG name
    LV name
    options
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not options:
        logging.error('lv_convert requires at least some options specified.')
        return False

    if not lv_name or not vg_name:
        logging.error('lv_convert requires vg_name and lv_name')
        return False

    cmd = f"lvconvert {' '.join(options)} {vg_name}/{lv_name}"
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not convert {lv_name}')
        return False

    return True


def lv_extend(vg_name: str, lv_name: str, options: list):  # noqa: ANN201
    """Increase size of logical volume.
    The arguments are:
    VG name
    LV name
    options
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not options:
        logging.error('lv_extend requires at least some options specified.')
        return False

    if not lv_name or not vg_name:
        logging.error('lv_extend requires vg_name and lv_name')
        return False

    cmd = f"lvextend {' '.join(options)} {vg_name}/{lv_name}"
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not extend {lv_name}')
        return False

    return True


def lv_reduce(vg_name: str, lv_name: str, options: list):  # noqa: ANN201
    """Decrease size of logical volume.
    The arguments are:
    VG name
    LV name
    options
    Returns:
    Boolean:
    True if success
    False in case of failure.
    """
    if not options:
        logging.error('lv_reduce requires at least some options specified.')
        return False

    if not lv_name or not vg_name:
        logging.error('lv_reduce requires vg_name and lv_name')
        return False

    cmd = f"lvreduce {' '.join(options)} {vg_name}/{lv_name}"
    retcode = run(cmd).rc
    if retcode != 0:
        logging.error(f'Could not reduce {lv_name}')
        return False

    return True


###########################################
# Config file
###########################################


def get_config_file_path():  # noqa: ANN201
    return '/etc/lvm/lvm.conf'


def update_config(key: str, value: str):  # noqa: ANN201
    config_file = get_config_file_path()
    search_regex = re.compile(r'(\s*)%s(\s*)=(\s*)\S*' % key)
    search_regex_with_comment = re.compile(r'(\s*#\s*)%s(\s*)=(\s*)\S*' % key)
    for line in fileinput.input(config_file, inplace=True):
        m = search_regex.match(line)
        m_with_comment = search_regex_with_comment.match(line)
        if m:
            line = f'{m.group(1)}{key} = {value}'  # noqa: PLW2901
        if m_with_comment:
            line = f"{m_with_comment.group(1).replace('#', '')}{key} = {value}"  # noqa: PLW2901
        # print saves the line to the file
        # need to remove new line character as print will add it
        line = line.rstrip('\n')  # noqa: PLW2901
        print(line)


def get_lvm_config_options(all_params=False):  # noqa: ANN001, ANN201
    """Get all the configuration types from lvm.conf file."""
    out = run('lvmconfig --type full').stdout.rstrip()

    options = {}
    category = ''
    for line in out.split('\n'):
        line = line.strip()  # noqa: PLW2901
        if not line or '}' in line:
            # skip empty or end of list line
            continue
        if '{' in line:
            # category part
            category = line[:-2]  # removing "allocation {"[:-2] == "allocation"
            options[category] = []
        elif '=' in line:
            # content of a category
            options[category].append(line.split('=')[0])

    if not all_params:
        return options

    options_all = []
    for value in options.values():
        options_all.extend(value)
    return options_all


def check_lvm_config(option):  # noqa: ANN001, ANN201
    return run(f'lvs -o {option}').stdout.rstrip()


def get_all_lvm_config_options():  # noqa: ANN201
    all_opts = check_lvm_config('asdf')  # needs just something that it doesn't know
    # we need to test_filter on lines that look like this
    # lvm_blahblah - explanation
    # and remove separators

    # at the end is '?' which should not be there therefore [:-1]
    return [i.split()[0] for i in all_opts if re.match(r'.+-.+', i) and '--' not in i][:-1]


def run_cmd(func):  # noqa: ANN001, ANN201
    # TODO: Duplicate of run_command
    """Decorator for running commands
    kwargs need to be edited every time, so decorator is probably the best solution.
    """

    @wraps(func)
    def wrapped(*args, **kwargs):  # noqa: ANN002, ANN003, ANN202
        return run_ret_out(func(), *args, **kwargs, return_output=True)  # cmd == func()

    return wrapped


@run_cmd
def get_all_lvmvdoconfig_options():  # noqa: ANN201
    return 'lvmconfig --type list'


@run_cmd
def lvdisplay():  # noqa: ANN201
    return 'lvdisplay'


def print_profile_file(profile_name, path=None):  # noqa: ANN001, ANN201
    if not path:
        path = '/etc/lvm/profile'  # default profile location
    run(f'cat {path}/{profile_name}.profile')


def get_lvdisplay_data():  # noqa: ANN201
    _, out = lvdisplay()
    lines = next(line for line in out if 'LV Name' in line and 'pool' not in line).split()
    print(lines)
    return lines[-1]


def run_command(func):  # noqa: ANN001, ANN201
    """Decorator for running commands
    kwargs need to be edited every time, so decorator is probably the best solution.
    """

    @wraps(func)
    def wrapped(inst, **kwargs):  # noqa: ANN001, ANN003, ANN202
        inst.tmp_kwargs = kwargs
        # The first thing is to replace values that are
        # conf=fmf_conf_value -> conf=conf_value
        kwargs = inst.replace_multiple_option_values(**kwargs)
        # check configuration arguments from old conf to new
        # slab_size=minimum -> slab_size=compute(value)
        kwargs = inst.check_config_arguments(**kwargs)

        # create command
        cmd, kwargs = func(inst, **kwargs)

        # remove everything not necessary
        kwargs = inst.remove_nones(inst.remove_vdo_arguments(**kwargs))

        # Check
        if inst.check(**kwargs) is not True:  # check() with "the manual"
            print('Check failed.')
            return False

        # Run
        return inst.run(cmd, **kwargs)

    return wrapped


class LVM(Wrapper):
    """Class for creating LVMVDO commands."""

    def __init__(self, disable_check=True, vdo_arguments_flag=True) -> None:  # noqa: ANN001
        self.disable_check = disable_check
        self.tmp_kwargs: dict = {}

        self.commands: dict[str, str | list[str]] = {
            'lvcreate': 'lvcreate',
            'lvremove': 'lvremove',
            'lvconvert': 'lvconvert',
            'lvchange': 'lvchange',
            'lvextend': 'lvextend',
            'lvreduce': 'lvreduce',
            'lvresize': 'lvresize',
        }

        self.commands['all'] = list(self.commands.keys())

        self.arguments = {  # "": [[""], "--"],
            'help': [self.commands['all'], ' --help'],
            'version': [self.commands['all'], ' --version'],
            'verbose': [self.commands['all'], ' --verbose'],
            'type': [['lvcreate', 'lvconvert'], '--type&'],
            'vdo': [['lvcreate'], '--vdo'],
            'vdopool': [['lvcreate'], '--vdopool&'],
            'vdo_name': [['lvcreate', 'lvconvert'], '--name&'],
            'size': [['lvcreate', 'lvextend'], '--size&'],
            'logical_size': [['lvcreate', 'lvconvert'], '--virtualsize&'],
            'config': [['lvcreate', 'lvextend'], '--config&'],
            'extents': [['lvcreate'], '--extents&'],
            'stripes': [['lvcreate', 'lvextend'], '--stripes&'],
            'stripesize': [['lvcreate', 'lvextend'], '--stripesize&'],
            'compression': [['lvcreate', 'lvconvert', 'lvchange'], '--compression&'],
            'deduplication': [
                ['lvcreate', 'lvconvert', 'lvchange'],
                '--deduplication&',
            ],
            'activate': [['lvchange'], '--activate&'],
            'metadataprofile': [
                ['lvcreate', 'lvconvert', 'lvchange'],
                '--metadataprofile&',
            ],
            'force': [['lvremove'], '--force'],
            'yes': [['lvremove'], '-y'],
            'refresh': [['lvchange'], ''],
            'vg_name': [['lvcreate', 'lvextend'], ''],
            'lv_name': [['lvchange'], ''],
        }

        self.no_check_size_unit = [
            'logical_size',
            'cachesize',
            'chunksize',
            'poolmetadatasize',
            'regionsize',
            'size',
            'stripesize',
            'virtualsize',
        ]

        self.argument_options = {
            # argument: [(.fmf option name values), (command option values)]
            # order in tuples matters
            # enable == 'y', disable == 'n'
            'activate': [('enabled', 'disabled', 'auto'), ('y', 'n', 'ay')],
            'deduplication': [('enabled', 'disabled'), ('y', 'n')],
            'compression': [('enabled', 'disabled'), ('y', 'n')],
            # '': [(,),(,)],
        }

        self.multiple_option_arguments = self.argument_options.keys()

        self.lvm_arguments = self.arguments.copy()

        self.option_translator_dictionary = {
            '1': 'vdo_use_compression',
            '2': 'vdo_use_deduplication',
            '3': 'vdo_use_metadata_hints',
            '4': 'vdo_minimum_io_size',
            'block_map_cache_size': 'vdo_block_map_cache_size_mb',
            'block_map_period': 'vdo_block_map_period',
            '5': 'vdo_check_point_frequency',
            'sparse_index': 'vdo_use_sparse_index',
            'index_mem': 'vdo_index_memory_size_mb',
            'slab_size': 'vdo_slab_size_mb',
            'ack_threads': 'vdo_ack_threads',
            'bio_threads': 'vdo_bio_threads',
            'bio_rotation_interval': 'vdo_bio_rotation',
            'cpu_threads': 'vdo_cpu_threads',
            'hash_zone_threads': 'vdo_hash_zone_threads',
            'logical_threads': 'vdo_logical_threads',
            'physical_threads': 'vdo_physical_threads',
            'write_policy': 'vdo_write_policy',
            'max_discard_size': 'vdo_max_discard',
            '6': 'vdo_pool_header_size',
        }
        self.config_arguments = self.option_translator_dictionary.keys()

        self.vdo_arguments = {}
        if vdo_arguments_flag:
            # obtain arguments from VDO for backwards compatibility
            self.vdo_arguments = vdo.VDO().arguments.copy()

            # cycle through keys common for both VDO and LVMVDO
            for vdo_arg in [arg for arg in self.vdo_arguments if arg in self.lvm_arguments]:
                self.vdo_arguments.pop(vdo_arg)  # pop so they don't get overwritten
            self.arguments.update(self.vdo_arguments)

        self.config_options = get_lvm_config_options()
        self.all_config_options = get_lvm_config_options(all_params=True)

        # backward compatibility between vdo and lvmvdo packages,
        # so that commands correspond to each other
        self.create = self.lvcreate

        Wrapper.__init__(self, self.commands, self.arguments, self.disable_check)

    @staticmethod
    def remove_nones(kwargs):  # noqa: ANN001, ANN205
        return {k: v for k, v in kwargs.items() if v is not None}

    @staticmethod
    def _add_value(value, command, argument):  # noqa: ANN001, ANN205
        """Copied from Wrapper."""
        if argument[-1:] in {'=', '&'}:
            if argument[-1:] == '&':
                argument = argument[:-1] + ' '
            if isinstance(value, list):
                # allows to use repeatable arguments as a list of values
                for val in value:
                    command += argument + "'" + str(val) + "'"
            else:
                command += argument + "'" + str(value) + "'"
        elif argument[-1:] == '*':
            command += str(value)
        else:
            command += argument
        return command + ' '  # added space at the end to fix formatting

    def _add_argument(self, arg, value, command):  # noqa: ANN001, ANN202
        """Copied from Wrapper."""
        # Checks if given argument is allowed for given command and adds it to cmd string
        self._check_allowed_argument(arg, command)
        return self._add_value(value, command, self._get_arg(arg))

    def _add_arguments(self, cmd, **kwargs):  # noqa: ANN001, ANN003, ANN202
        """Copied from Wrapper."""
        command = cmd
        for kwarg in kwargs:
            # skip adding this argument if the value is False
            if kwargs[kwarg] is False:
                continue
            # skip:
            # vg_name, it should be last
            # vdo_name should be just "name" but not used is OK :D
            if kwarg in 'vg_name':  # ,"vdo_name"):  # maybe more names will be here
                continue
            command = self._add_argument(kwarg, kwargs[kwarg], command)

        # vg_name must be the last in command
        if 'vg_name' in kwargs:
            command += kwargs['vg_name']
        return command

    def _get_possible_arguments(self, command=None):  # noqa: ANN001, ANN202
        return super()._get_possible_arguments(command.split()[0])

    def run(self, cmd, **kwargs):  # noqa: ANN001, ANN003, ANN201
        """Constructs the command to run and runs it."""
        cmd = self._add_arguments(cmd, **kwargs)

        print(cmd)
        ret = run(cmd).rc

        if isinstance(ret, tuple) and ret[0] != 0:
            logging.warning(f"Running command: '{cmd}' failed. Return with output.")
        elif isinstance(ret, int) and ret != 0:
            logging.warning(f"Running command: '{cmd}' failed.")
        return ret

    def number_of_conf_args(self, **kwargs):  # noqa: ANN003, ANN201
        """Counts the number of configuration arguments in kwargs and returns it."""
        return sum(conf_arg in kwargs for conf_arg in self.config_arguments)

    def _set_kwargs_value(self, arg, **kwargs):  # noqa: ANN001, ANN003, ANN202
        """If the value in test declaration is 'enabled'
        it switches it to the one in the man page, e.g. 'y'
        self.argument_options['activate'].
        """
        fmf_options = self.argument_options[arg][0]
        opt_values = self.argument_options[arg][1]

        print(fmf_options)
        for idx, value in enumerate(fmf_options):
            kwargs[arg] = opt_values[idx] if kwargs[arg] == value else kwargs[arg]

        return kwargs

    def get_option(self, argument):  # noqa: ANN001, ANN201
        """Get an option to set up in a configuration file."""
        if argument in self.option_translator_dictionary:
            return self.option_translator_dictionary[argument]
        return argument  # maybe this should be None, so it is obvious that there is an error

    def minimum_slab_size(self, device_name, default_to_2g=True):  # reused from vdo.py  # noqa: ANN001, ANN201
        """Computing minimum slab size, used from vdo.py."""

        class VDODeviceNotFoundError(Exception):
            pass

        print(device_name)
        ret, device_size = run_ret_out(cmd=f"lsblk | grep '{device_name} ' ", return_output=True)
        print(device_name, ret, device_size)
        if ret != 0:
            raise VDODeviceNotFoundError

        # ['└─myvg-vdotest', '252:2', '0', '4G', '0', 'lvm'][3] == '4G'
        size = device_size.split()[3]
        multipliers = ['M', 'G', 'T', 'P', 'E']

        device_size = int(float(size[:-1]) * (1024 ** multipliers.index(size[-1:])))
        max_number_of_slabs = 8192
        minimum_size = max(2 ** int(device_size / max_number_of_slabs).bit_length(), 128)  # reused from vdo.py
        if default_to_2g and minimum_size < 2048:
            return '2G'
        return f'{minimum_size!s}M'

    def check_conf_value(self, val):  # noqa: ANN001, ANN201
        """Remove units K, G, T and convert accordingly."""
        if 'fail' in self.tmp_kwargs['name']:
            return val  # don't check

        units = {
            'K': 0.001,  # 1/1024 = 0.00097656,
            'k': 0.001,
            'M': 1,
            'm': 1,
            'G': 1024,  # 1000
            'g': 1024,
            'T': 1048576,  # 1000000
            't': 1048576,
            # "B": 1  # should do nothing
        }

        if re.match(r'[0-9]+\.[0-9]+', str(val)):  # float
            return val

        match = re.match(r'([0-9]+)(.+|)', str(val))
        if not match:
            return val

        multiplier = 1
        if len(match.groups()) == 2 and match.group(2):  # should not be empty
            try:
                multiplier = units[match.group(2)]
            except KeyError:  # because of "512B"
                print('Argument value: ', match.group(2), '.')
                print(f'Original {val}; will return {val[:-1]}')
                return val[:-1]
        return str(int(match.group(1)) * multiplier)

    def check_config_arguments(self, **kwargs):  # noqa: ANN003, ANN201
        """Check arguments in config."""
        if 'slab_size' in kwargs:
            device_name = kwargs['device'].split('/')[-1]
            # Slab_size value should be in MB
            kwargs['slab_size'] = self.check_conf_value(self.minimum_slab_size(device_name))

        return kwargs

    def create_profile_file(self, profile_name, args_to_remove, **kwargs):  # noqa: ANN001, ANN003, ANN201
        """Example: category {
            arg1 = value,
            arg2 = value
        }.
        """
        run(f'rm /etc/lvm/profile/{profile_name}.profile')

        # creates metadataprofile ONLY ONE CATEGORY NOW!!!!
        # update 28022022 don't know if it is true, after code review this should do multiple categories...
        to_write = {}  # category: [list of values]
        with Path(f'/etc/lvm/profile/{profile_name}.profile').open('w', encoding='utf-8') as fp:
            # create the structure of the document and save it in a string
            for arg, value in kwargs.items():
                if arg in self.config_arguments:  # do just what is necessary
                    category = self.get_category(arg)
                    if category not in to_write:
                        to_write[category] = []

                    to_write[category].append(f'{self.get_option(arg)}={self.check_conf_value(value)}')
                    args_to_remove.append(arg)

            str_to_write = ''
            for category in to_write:
                for value in to_write.values():
                    str_to_write += f'{category} {{\n'
                    for opt in value:
                        str_to_write += f'\t{opt}\n'
                str_to_write += '}\n'
            fp.write(str_to_write)  # in 'with' section there is no need for fp.close()

        return args_to_remove

    def replace_multiple_option_values(self, **kwargs):  # noqa: ANN003, ANN201
        """Check and replace what is defined in .fmf test file with corresponding value from man page
        e.g. 'enabled' -> 'y'.
        """
        for arg in self.multiple_option_arguments:
            if arg in kwargs:
                kwargs = self._set_kwargs_value(arg, **kwargs)
        # kwargs = {self._set_kwargs_value(i, **kwargs) for i in self.multiple_option_arguments if i in kwargs}
        return kwargs

    def remove_vdo_arguments(self, **kwargs):  # noqa: ANN003, ANN201
        """The rest of VDO arguments need to be removed otherwise unsupported arguments
        will propagate into the command.
        """
        arg_to_remove = [arg for arg in kwargs if arg in self.vdo_arguments]
        for arg in arg_to_remove:
            kwargs.pop(arg)
        return kwargs

    def get_category(self, argument):  # noqa: ANN001, ANN201
        """Get the list that contains the argument I am looking for.

        # not working for "check" (there are multiple) :( not fixed :/
        """
        for one_list in list(self.config_options.values()):
            if argument in one_list or self.option_translator_dictionary[argument] in one_list:
                arguments_of_category = one_list
                break  # find the first one

        # using the list containing the argument as item of the list
        index = list(self.config_options.values()).index(arguments_of_category)
        return list(self.config_options.keys())[index]

    def check(self, **kwargs):  # noqa: ANN003, ANN201
        """Check arguments compatibility with command."""
        if 'name' in kwargs:
            kwargs.pop('name')  # remove name, because it is not used in lvmvdo

        if 'size' in kwargs:
            # value format for size parameter
            return bool(re.match(r'^([\+|\-]|)[0-9]+[T|G|M|K]$', kwargs['size']))
        return True

    @staticmethod
    def remove_args(to_remove, **kwargs):  # noqa: ANN001, ANN003, ANN205
        """Return only what is intended."""
        return {k: v for k, v in kwargs.items() if k not in to_remove}

    @run_command
    def lvcreate(self, **kwargs):  # noqa: ANN003, ANN201
        print('LVCREATE', kwargs)
        cmd = 'lvcreate --vdo '

        # config part START
        args_to_remove = []
        use_conf_file = False

        if use_conf_file:
            profile_name = 'vdo_create'
            args_to_remove = self.create_profile_file(profile_name, args_to_remove, **kwargs)
            cmd += f'--metadataprofile {profile_name} '
            print_profile_file(profile_name)
        elif self.number_of_conf_args(**kwargs) != 0:
            cmd += '--config'
            # --config="    for condition == 1
            # --config '   else
            cmd += '="' if self.number_of_conf_args(**kwargs) == 1 else " '"

            for arg, value in kwargs.items():
                if arg in self.config_arguments:  # do just what is necessary
                    if self.number_of_conf_args(**kwargs) == 1:
                        # --config="cat/opt=val
                        cmd += f'{self.get_category(arg)}/{self.get_option(arg)}={self.check_conf_value(value)}'
                    else:
                        # --config 'cat/opt=val cat/opt=val cat/opt=val
                        cmd += f'{self.get_category(arg)}/{self.get_option(arg)}={self.check_conf_value(value)} '
                    args_to_remove.append(arg)

            # --config="cat/opt=val"                          == 1
            # --config 'cat/opt=val cat/opt=val cat/opt=val'  else
            cmd += '" ' if self.number_of_conf_args(**kwargs) == 1 else "' "

        # some arguments are used as config and are no longer needed
        kwargs = self.remove_args(args_to_remove, **kwargs)
        # config part END

        kwargs['yes'] = '-y'  # see lvremove

        return cmd, kwargs

    @run_command
    def lvremove(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'lvremove '

        # lvmvdo uses human interface for some activities like removing vdo pools
        # in automation we don't want this, so we add '-y' to force it
        kwargs['yes'] = '-y'
        return cmd, kwargs

    @run_command
    def lvconvert(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'lvconvert --vdo '
        return cmd, kwargs

    @run_command
    def lvchange(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'lvchange '
        if 'vdo_name' in kwargs:
            kwargs.pop('vdo_name')
        return cmd, kwargs

    @run_command
    def lvextend(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'lvextend '
        return cmd, kwargs

    @run_command
    def lvmconfig(self, **kwargs):  # noqa: ANN003, ANN201
        cmd = 'lvmconfig '
        return cmd, kwargs
