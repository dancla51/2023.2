Define ObjectType {
  FIFOQTrigger
  RadiologyControlUnit
}

ControllerIconModel ImageFile { '<res>/images/Controller-256.png' }  Transparent { TRUE }
AssembleIconModel ImageFile { '<res>/images/Assemble-256.png' }  Transparent { TRUE }

FIFOQTrigger JavaClass { ssq.FIFOQTrigger }  Palette { 'Single Server Queue' } DefaultDisplayModel { ControllerIconModel } IconFile { '<res>/images/Controller-24.png' } DefaultSize { 0.5 0.5 0.5 m }
RadiologyControlUnit JavaClass { labs.RadiologyControlUnit }  Palette { 'Custom Logic' } DefaultDisplayModel { AssembleIconModel } IconFile { '<res>/images/Assemble-24.png' } DefaultSize { 0.5 0.5 0.5 m }