package lol;

import jriot.main.JRiot;
import jriot.main.JRiotException;
import jriot.objects.Summoner;


public class Main {

	public static void main(String[] args) throws JRiotException {
		JRiot lol = new JRiot();
		lol.setApiKey("fa3518a3-2076-40e9-adfd-2f19bf27a502");
		lol.setRegion("euw");
		Summoner summoner = lol.getSummoner("percivalalb");
		System.out.println(summoner);
	}
}
