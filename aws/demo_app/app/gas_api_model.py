from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config, Undefined
from datetime import date
from marshmallow import fields

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Supplier:
    shipper_name: str = None
    amr_indicator: str = None
    amr_sp: str = None 
    csep_id: str = None
    current_supplier_name: str = None
    dcc_service_flag: str = None
    dcc_service_flag_efd: str = None
    first_smets_installation_date: str = None
    formula_year_offtake_quantity: str = None
    formula_year_annual_quantity: str = None 
    ihd_install_status: str = None
    incoming_supplier: str = None 
    installing_supplier_id: str = None
    interruption_contract_exists: str = None
    isolation_status: str = None
    latest_meter_read_date: str = None
    latest_meter_read_type: str = None
    latest_meter_read_value: str = None
    mam_short_code: str = None
    meter_device_status: str = None
    meter_imperial_indicator: str = None
    meter_number_of_dials: int = None
    meter_type: str = None
    mprn: str = None 
    network_name: str = None 
    network_owner_effective_from_date: str = None
    smso_id: str = None
    sms_operating_entity_efd: str = None
    supply_point_withdrawal_status: str = None 
    twin_stream_site_indicator: str = None 
    address_id: str = None 
    postcode: str = None
    house_no: str = None
    house_name: str = None
    sub_building_name: str = None
    street: str = None 
    town: str = None
    county: str = None 
    country: str = None 
    dependent_street: str = None
    dependent_local: str = None
    double_dependent_local: str = None 
    po_box_no: str = None 
    delivery_point_alias: str = None
    current_supplier: str = None
    meter_point_status: str = None
    market_sector_code: str = None
    ldz_id: str = None
    meter_capacity: str = None 
    meter_mechanism: str = None
    msn: str = None
    annual_quantity: str = None
    uprn: str = None
    shipper_short_code: str = None
    end_user_category_code: str = None 
    previous_supplier_name: str = None 
    previous_supplier_short_code: str = None
    confirmation_reference_number: str = None 
    confirmation_effective_date: str = None
    priority_consumers_indicator: str = None
    meter_read_batch_frequency: str = None
    csep_max_annual_quantity: str = None 
    original_supply_meter_point_annual_quantity: str = None
    supply_meter_point_current_year_minimum_annual_quantity: str = None
    csep_supply_point_offtake_quantity: str = None 
    meter_manufacturer: str = None 
    meter_model: str = None 
    meter_year_of_manufacture: str = None
    meter_installation_date: str = None
    meter_units: str = None
    meter_location: str = None 
    correction_factor: str = None
    gas_act_owner: str = None 
    meter_asset_manager_effective_date: str = None
    supply_meter_point_shq: str = None
    shipper_nam: str = None
    igt_transportation_charge_rate: str = None
    igt_transportation_charge_rate_type: str = None
    igt_charging_methodology: str = None 
    meter_link_code: str = None
    end_user_category_identifier: str = None 
    offtake_quantity: str = None
    small_large_supply_point_indicator: str = None
    daily_metered_indicator: str = None
    convertor_indicator: str = None

@dataclass_json
@dataclass
class Mprn:
    amr_indicator: str = None
    country: str = None
    county: str = None
    csep_id: str = None
    current_aq_roll_value: int = None
    current_formula_year_aq_value: int = None
    current_formula_year_soq_value: int = None
    current_soq_roll_value: int = None
    dependent_local: str = None
    dependent_street: str = None
    distribution_network_operator: str = None 
    exit_zone: str = None
    house_no: str = None
    local_distribution_zone: str = None
    market_sector_code: str = None
    mprn: str = None
    perspective_formula_year_aq_value: int = None
    perspective_formula_year_effective_date: str = None
    perspective_formula_year_soq_value: int = None
    postcode: str = None
    street: str = None
    sub_building_name: str = None
    town: str = None
    installation_number: str = None