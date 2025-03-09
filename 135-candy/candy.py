class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr=[1]*len(ratings)
        #skip the first index 0, as it has no left neighbour
        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]:
                arr[i]=arr[i-1]+1
        #skip the last index n-1, as it has no right neighbour
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                arr[i]=max(arr[i],arr[i+1]+1)
        return sum(arr)