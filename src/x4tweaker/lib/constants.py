from enum import Enum

class Dlc(Enum):
    SPLIT       = ('ego_dlc_split', 'Split Vendetta')
    TERRAN      = ('ego_dlc_terran', 'Cradle of Humanity')
    PIRATE      = ('ego_dlc_pirate', 'Tides of Avarice')
    BORON       = ('ego_dlc_boron', 'Kingdom End')
    TIMELINES   = ('ego_dlc_timelines', 'Timelines')

class SWeapons(Enum):
    PULSE_LASER_S_WEAK          = ('bullet_gen_s_laser_01_mk1')
    PULSE_LASER_S_STRONG        = ('bullet_gen_s_laser_01_mk2')
    BOLT_REPEATER_S_WEAK        = ('bullet_gen_s_gatling_01_mk1')
    BOLT_REPEATER_S_STRONG      = ('bullet_gen_s_gatling_01_mk2')
    BEAM_EMITTER_S_WEAK         = ('bullet_gen_s_beam_01_mk1')
    BEAM_EMITTER_S_STRONG       = ('bullet_gen_s_beam_01_mk2')
    SHARD_BATTERY_S_WEAK        = ('bullet_gen_s_shard_01_mk1')
    SHARD_BATTERY_S_STRONG      = ('bullet_gen_s_shard_01_mk2')
    ION_BLASTER_S_WEAK          = ('bullet_arg_s_ion_01_mk1')
    ION_BLASTER_S_STRONG        = ('bullet_arg_s_ion_01_mk2')
    MUON_CHARGER_S_WEAK         = ('bullet_tel_s_charge_01_mk1')
    MUON_CHARGER_S_STRONG       = ('bullet_tel_s_charge_01_mk2')
    BLAST_MORTAR_S_WEAK         = ('bullet_gen_s_cannon_01_mk1')
    BLAST_MORTAR_S_STRONG       = ('bullet_gen_s_cannon_01_mk2')
    PLASMA_CANNON_S_WEAK        = ('bullet_gen_s_plasma_01_mk1')
    PLASMA_CANNON_S_STRONG      = ('bullet_gen_s_plasma_01_mk2')
    BURST_RAY_S_WEAK            = ('bullet_gen_s_burst_01_mk1')
    BURST_RAY_S_STRONG          = ('bullet_gen_s_burst_01_mk2')
    MASS_DRIVER_S_WEAK          = ('bullet_par_s_railgun_01_mk1')
    MASS_DRIVER_S_STRONG        = ('bullet_par_s_railgun_01_mk2')
    MINING_DRILL_S_WEAK         = ('bullet_gen_s_mining_01_mk1')
    MINING_DRILL_S_STRONG       = ('bullet_gen_s_mining_01_mk2')
    KYON_EMITTER_S_WEAK         = ('bullet_kha_s_beam_01_mk1')

class MWeapons(Enum):
    PULSE_LASER_M_WEAK          = ('bullet_gen_m_laser_01_mk1')