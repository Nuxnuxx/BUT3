package utilisation;

import api.DeuxEntierPourUn;

import java.util.List;
import java.util.function.Consumer;

public class Principale {

    public static void main(String[] args) {
        DeuxEntierPourUn premierExemple;

        premierExemple=(p1,p2)->{

            return p1+p2;
        };

        int res=premierExemple.calcul(3, 5);

        System.out.println("res=" + res);

        desChaines = List.of("Toto", "titi", "tata");

        desChaines.forEach(s->);
    }
}
