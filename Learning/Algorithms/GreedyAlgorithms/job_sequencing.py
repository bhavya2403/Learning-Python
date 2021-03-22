class Job:
    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


def JobScheduling(jobs, n): # O(n(log(n)+max_deadline))
    # Jobs = (1, 4, 20)(2, 1, 10)(3, 1, 40)(4, 1, 30)
    jobs.sort(key=lambda job: job.profit, reverse=True) # O(nlog(n))
    max_deadline = 0
    for i in jobs: # O(n)
        if i.deadline > max_deadline:
            max_deadline = i.deadline

    slots = [0] * max_deadline
    jobs_done = 0
    tot_profit = 0
    for i in jobs: # O(n*(max_deadline))
        for j in range(i.deadline-1, -1, -1):
            if not slots[j]:
                slots[j] = 1
                jobs_done += 1
                tot_profit += i.profit
                break
    return jobs_done, tot_profit

for _ in range(int(input())):
    n = int(input())
    info = list(map(int, input().strip().split()))
    jobs = [Job() for i in range(n)]
    for i in range(n):
        jobs[i].id = info[3*i]
        jobs[i].deadline = info[3*i+1]
        jobs[i].profit = info[3*i+2]
    res = JobScheduling(jobs, n)
    print(res[0])
    print(res[1])

print(JobScheduling([(1,4,20), (2,1,10), (3,1,40), (4,1,30)], 4))
