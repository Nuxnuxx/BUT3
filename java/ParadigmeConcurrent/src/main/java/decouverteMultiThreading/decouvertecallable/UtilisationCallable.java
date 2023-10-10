package decouverteMultiThreading.decouvertecallable;

import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.ExecutorService;


public class UtilisationCallable {
    public static void main(String[] args) throws InterruptedException {

    System.out.println("Debut de " + Thread.currentThread().getName());

    Additionneur additionneur25 = new Additionneur(25);
    Additionneur additionneur12 = new Additionneur(12);


    ExecutorService monExecutorService = Executors.newFixedThreadPool(3);

    monExecutorService.submit(additionneur25);

    TimeUnit.MILLISECONDS.sleep(2500);

    monExecutorService.submit(additionneur12);

    TimeUnit.SECONDS.sleep(2);

    Additionneur additionneur20 = new Additionneur(20);
    Additionneur additionneur7 = new Additionneur(7);
    Additionneur additionneur13 = new Additionneur(13);
    Additionneur additionneur6 = new Additionneur(6);

    monExecutorService.submit(additionneur20);
    monExecutorService.submit(additionneur7);
    monExecutorService.submit(additionneur13);
    monExecutorService.submit(additionneur6);

    TimeUnit.SECONDS.sleep(15);

    System.out.println("Fin de " + Thread.currentThread().getName());
    }
}
