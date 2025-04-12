import esphome.codegen as cg
import esphome.config_validation as cv

from esphome import automation
from esphome.const import CONF_ID

# Correct namespace and class name
mower_ns = cg.esphome_ns.namespace('mower')
Automower = mower_ns.class_('Automower', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(Automower),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
