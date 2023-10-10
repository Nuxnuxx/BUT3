package decouverteMultiThreading.decouvertecallable;

import java.util.concurrent.Callable;
import java.util.concurrent.TimeUnit;

public class Additionneur implements Callable<Integer> {

    private int n;

    public Additionneur(int n) {
        this.n = n;
    }


    @Override
    public Integer call() throws Exception {
        System.out.println("Debut Additionneur : " + n);

        int res = 0;

        for (int i = 0; i <=n ; i++) {
            System.out.println("i=" + i + Thread.currentThread().getName());
            res += i;

            TimeUnit.MILLISECONDS.sleep(333);
        }

        System.out.println("Fin Additionneur : " + n + " res="+res);

        return res;
    }
}
