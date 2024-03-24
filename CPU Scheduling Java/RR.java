/**
 * Non-preemptive priority scheduling algorithm using RR.
 *
 * This algorithm will run tasks according to round-robin scheduling.
 */
 
import java.util.*;
import java.util.List;
import java.util.LinkedList;
import java.util.Queue;

public class RR implements Algorithm {
    private Queue<Task> taskQueue;
    private int quantum;  // Quantum time slice

    // Constructor to initialize the RR scheduler with quantum value
    public RR(List<Task> queue, int quantum) {
        this.taskQueue = new LinkedList<>(queue);
        this.quantum = quantum;  // Set the quantum value
    }

    @Override
    public void schedule() {
        // Process tasks until the quantum time finishes
        while (!taskQueue.isEmpty()) {
            Task currentTask = taskQueue.poll();
            int remainingBurst = Math.min(currentTask.getBurst(), quantum);

            // Run the task on the CPU
            CPU.run(currentTask, remainingBurst);

            // Check if task is completed or needs to be re-queued
            if (currentTask.getBurst() > remainingBurst) {
                currentTask.setBurst(currentTask.getBurst() - remainingBurst);
                taskQueue.offer(currentTask);   // Re-queue the task
            } else {
                System.out.println("Task quantum finished: " + currentTask.getName() + "\n");
            }
        }
    }

    @Override
    public Task pickNextTask() {
        // Return the next task or null
        return taskQueue.isEmpty() ? null : taskQueue.poll();
    }
}