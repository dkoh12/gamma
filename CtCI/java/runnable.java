import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.Thread;
import java.lang.Runnable;

// class RunnableThreadExample implements Runnable {
// 	public int count = 0;

// 	public void run() {
// 		System.out.println("RunnableThread starting.");

// 		try {
// 			while (count < 5) {
// 				Thread.sleep(500);
// 				count++;
// 			}
// 		} catch (InterruptedException exc) {
// 			System.out.println("RunnableThread interrupted");
// 		}
// 		System.out.println("RunnableThread terminating.");
// 	}

// 	public static void main(String[] args) {
// 		RunnableThreadExample instance = new RunnableThreadExample();
// 		Thread thread = new Thread(instance);
// 		thread.start();

// 		while (instance.count != 5) {
// 			try {
// 				Thread.sleep(250);
// 			} catch (InterruptedException exc) {
// 				exc.printStackTrace();
// 			}
// 		}

// 	}
// }



class ThreadExample extends Thread {
	int count = 0;

	public void run() {
		System.out.println("Thread starting.");
		try {
			while (count < 5) {
				Thread.sleep(500);
				System.out.println("In Thread, count is " + count);
				count++;
			}
		} catch (InterruptedException exc) {
			System.out.println("Thread interrupted");
		}
		System.out.println("Thread terminating");
	}
}

class ExampleB {
	public static void main(String args[]) {
		ThreadExample instance = new ThreadExample();
		instance.start();

		while(instance.count != 5) {
			try {
				Thread.sleep(500);
			} catch(InterruptedException exc) {
				exc.printStackTrace();
			}
		}
	}
}



