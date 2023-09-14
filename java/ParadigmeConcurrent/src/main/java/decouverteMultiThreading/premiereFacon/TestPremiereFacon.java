package decouverteMultiThreading.premiereFacon;

public class TestPremiereFacon {

    public static void main(String[] args) throws InterruptedException {

        System.out.println("Debut test premiere facon" + Thread.currentThread().threadId());

        MonThread premierMonThread = new MonThread("abcdef");
        MonThread secondMonThread = new MonThread("      ghijkl");

        // premierMonThread.run();  HORREUR!!!!!!!!!
        // secondMonThread.run();

        premierMonThread.start();
        secondMonThread.start();

        Thread.currentThread().sleep(3000);

        premierMonThread.mettreFin();

        Thread.currentThread().sleep(2000);

        secondMonThread.mettreFin();

        System.out.println("Fin test premiere facon");
    }
}
