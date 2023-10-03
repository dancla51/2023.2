package labs;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import com.jaamsim.units.DimensionlessUnit;

import hccm.controlunits.ControlUnit;
import hccm.controlunits.ControlUnit.ActivityStartCompare;
import hccm.entities.ActiveEntity;

public class dcla189_ControlUnit extends ControlUnit {
	
	public void OnStartWaitForTurnstile(List<ActiveEntity> ents, double simTime) {
		
		// Get all idle turnstiles
		ArrayList<ActiveEntity> idleTurns = this.getEntitiesInActivity("Turnstile", "WaitForPerson", simTime);
		ActivityStartCompare actStartComp = this.new ActivityStartCompare();
		
		ActiveEntity person = ents.get(0);
		double turnstileID = getNumAttribute(person, "Turnstile", simTime, -1);
		
		if (idleTurns.size() > 0) {
			// See if correct ID turnstile is free
			List<ActiveEntity> thisTurnstile = idleTurns
					  .stream()
					  .filter(q -> getNumAttribute(q, "ID", simTime, -1) == turnstileID)
					  .collect(Collectors.toList());
			
			ActiveEntity turnstile = thisTurnstile.get(0);
					
			transitionTo("Entry", person, turnstile);
		}
	}
	
	public void OnStartWaitForPerson(List<ActiveEntity> ents, double simTime) {
		
		ArrayList<ActiveEntity> idlePeople = this.getEntitiesInActivity("Person", "WaitForTurnstile", simTime);
		ActivityStartCompare actStartComp = this.new ActivityStartCompare();
		ActiveEntity turnstile = ents.get(0);
		double turnstileID = getNumAttribute(turnstile, "ID", simTime, -1);
		
		if (idlePeople.size() > 0) {
			Collections.sort(idlePeople, actStartComp);
			// sort based on if they are at this turnstile
			List<ActiveEntity> peopleThisTurnstile = idlePeople
					  .stream()
					  .filter(q -> getNumAttribute(q, "Turnstile", simTime, -1) == turnstileID)
					  .collect(Collectors.toList());
			
			// If someone waiting at this turnstile then transition
			if (peopleThisTurnstile.size() > 0) {
			
				ActiveEntity person = peopleThisTurnstile.get(0);
				transitionTo("Entry", person, turnstile);
				
			}
		}
	}
	
	public void OnStartChooseDirection(List<ActiveEntity> ents, double simTime) {
		
		// Get attributes
		ActiveEntity person = ents.get(0);
		int currentsection = (int) getNumAttribute(person, "CurrentSection", simTime, -1);   
		int seatsection = (int) getNumAttribute(person, "SeatSection", simTime, -1);  
		// Test if in correct section
		if (currentsection == seatsection) {
			transitionTo("TakeSeat", person);
		}
		
		// Otherwise traverse the section
		int direction = (int) getNumAttribute(person, "Direction", simTime, -1);  
		
		// Move down or up
		transitionTo("TraverseSection", person);
					
					
		if (direction == 1) {
			// If necessary switch direction
			if (seatsection < currentsection) {
				setNumAttribute(person, "Direction", -1, DimensionlessUnit.class);
			}
		} else {
			// If necessary switch direction
			if (seatsection > currentsection) {
				setNumAttribute(person, "Direction", 1, DimensionlessUnit.class);
			}
		}
	
	}
	
	
}





