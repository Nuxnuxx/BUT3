package decouverteMultiThreading.pabo;

import java.util.concurrent.TimeUnit;

public class TestPasBo {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Debut de TestSecondeFacon :" + Thread.currentThread().getName());


        MonThread premierMonThread = new MonThread("abcdef");
        MonThread secondMonThread = new MonThread("       GHIJKL");

        Runnable r1 = premierMonThread;
        Thread t1 = new Thread(r1);

        Thread t2 = new Thread(secondMonThread);

        t1.start();

        TimeUnit.SECONDS.sleep(3);

        t2.start();

        TimeUnit.SECONDS.sleep(3);

        //t1.mettreFin()
        premierMonThread.mettreFin();

        TimeUnit.SECONDS.sleep(5);

        secondMonThread.mettreFin();

        System.out.println("Fin de TestSecondeFacon :" + Thread.currentThread().getName());
    }
}