
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;


class Chopstick {
	private Lock lock;

	public Chopstick() {
		lock = new ReentrantLock();
	}

	public void pickUp() {
		lock.lock();
	}

	public void putDown() {
		lock.unlock();
	}

}

class Philosopher extends Thread {
	private int bites = 10;
	private Chopstick left, right; 

	public Philosopher(Chopstick left, Chopstick right) {
		this.left = left;
		this.right = right;
	}

	public void eat() {
		pickUp();
		chew();
		putDown();
	}

	public void pickUp(){
		left.pickUp();
		right.pickUp();
	}

	public void chew(){ }

	public void putDown() {
		right.putDown();
		left.putDown();
	}

	public void run() {
		for(int i=0; i<bites; i++) {
			eat();
		}
	}
}