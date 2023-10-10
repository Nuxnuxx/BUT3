package decouverteMultiThreading.decouvertecallable;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.TimeoutException;

public class Resultats {

    public static void pause(TimeUnit tu,long duree){
        try {
            tu.sleep(duree);
        } catch (InterruptedException e) {
        }
    }

    public static void main(String[] args) {

        System.out.println("Debut de " + Thread.currentThread().getName());

        Additionneur additionneur25 = new Additionneur(25);
        Additionneur additionneur12 = new Additionneur(12);


        ExecutorService monExecutorService = Executors.newFixedThreadPool(3);

        Future<Integer> future25 =  monExecutorService.submit(additionneur25);

        pause(TimeUnit.SECONDS, 2);


        // get avec timeout si trop atrd throw lexception timeout
        try {
            System.out.println("Avant get");
            int res25 = future25.get(3, TimeUnit.SECONDS);
            System.out.println("Apres get : res25 =" + res25);
        } catch(InterruptedException e){
            throw new RuntimeException(e);
        } catch (ExecutionException e) {
        } catch (TimeoutException e){
            System.out.println("TROP TARD!!!!!!!!!!");
            future25.cancel(true);
        }

        pause(TimeUnit.MILLISECONDS, 2500);

        monExecutorService.submit(additionneur12);

        pause(TimeUnit.SECONDS, 15);

        System.out.println("Fin de " + Thread.currentThread().getName());
    }
}
