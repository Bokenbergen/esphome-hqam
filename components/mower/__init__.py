import esphome.codegen as cg
import esphome.config_validation as cv

from esphome import automation
from esphome.const import CONF_ID

# Create namespace and define component class
automower_ns = cg.esphome_ns.namespace('automower')
automowercomponent = automower_ns.class_('automowercomponent', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(automowercomponent),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
