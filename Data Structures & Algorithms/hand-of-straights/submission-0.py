class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        for a in range(len(hand)//groupSize):
            i = 0
            curr = []
            while i < len(hand) and len(curr) < groupSize:
                if hand[i] < 0:
                    i+=1
                    continue
                if len(curr) == 0:
                    curr.append(hand[i])
                    hand[i] = -hand[i]
                    i+=1
                    continue
                else:
                    if hand[i] == curr[-1]:
                        i+=1
                        continue
                    elif hand[i] == curr[-1] +1:
                        curr.append(hand[i])
                        hand[i] = -hand[i]
                        continue
                    else:
                        return False
        return True
