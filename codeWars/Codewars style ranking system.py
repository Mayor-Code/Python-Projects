class User:
    ranks = list(range(-8, 0)) + list(range(1, 9))

    def __init__(self):
        self.rank = self.ranks[0]
        self.progress = 0

    def inc_progress(self, activity_rank):
        if not activity_rank in self.ranks:
            raise Exception("out of rank range")
        if self.rank == self.ranks[-1]:
            self.progress = 0
            return
        diff = self.ranks.index(activity_rank) - self.ranks.index(self.rank)
        if diff == 0:
            self.progress += 3
        elif diff == -1:
            self.progress += 1

        elif diff > 0:
            self.progress += 10 * diff * diff

        while self.progress >= 100:
            self.rank = self.ranks[self.ranks.index(self.rank) + 1]
            self.progress -= 100
            if self.rank == self.ranks[-1]:
                self.progress = 0
                break


user = User()
user.inc_progress(-7)
print(user.rank)
print(user.progress)
