package labs;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import hccm.controlunits.ControlUnit;
import hccm.controlunits.ControlUnit.ActivityStartCompare;
import hccm.entities.ActiveEntity;

public class dcla189_ControlUnit extends ControlUnit {
	
	public void StartWaitForTurnstile(List<ActiveEntity> ents, double simTime) {
		
		ArrayList<ActiveEntity> idleTurns = this.getEntitiesInActivity("Turnstile", "WaitForPerson", simTime);
		ActivityStartCompare actStartComp = this.new ActivityStartCompare();
		
		if (idleTurns.size() > 0) {
			Collections.sort(idleTurns, actStartComp);
			
			ActiveEntity person = ents.get(0);
			ActiveEntity turnstile = idleTurns.get(0);
					
			transitionTo("Entry", person, turnstile);
		}
	}
	
	public void StartWaitForPerson(List<ActiveEntity> ents, double simTime) {
		
		ArrayList<ActiveEntity> idlePeople = this.getEntitiesInActivity("Person", "WaitForTurnstile", simTime);
		ActivityStartCompare actStartComp = this.new ActivityStartCompare();
		
		if (idlePeople.size() > 0) {
			Collections.sort(idlePeople, actStartComp);
			
			ActiveEntity turnstile = ents.get(0);
			ActiveEntity person = idlePeople.get(0);
					
			transitionTo("Entry", person, turnstile);
		}
	}
	
	public void StartChooseDirection(List<ActiveEntity> ents, double simTime) {
		
		
		
		
		transitionTo()
		
	}
	
}
