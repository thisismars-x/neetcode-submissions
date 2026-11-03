class Twitter:

    def __init__(self):
        from collections import defaultdict

        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq

        users = self.following[userId] | {userId}
        heap = []

        for uid in users:
            tweets = self.tweets[uid]

            if tweets:
                i = len(tweets) - 1
                t, tweet = tweets[i]
                heapq.heappush(heap, (-t, tweet, uid, i))

        feed = []

        while heap and len(feed) < 10:
            t, tweet, uid, i = heapq.heappop(heap)
            feed.append(tweet)

            if i > 0:
                t, tweet = self.tweets[uid][i - 1]
                heapq.heappush(heap, (-t, tweet, uid, i - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)