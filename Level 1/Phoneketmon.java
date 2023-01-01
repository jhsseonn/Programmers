import java.util.HashSet;

public class Phoneketmon {
    public int solution(int[] nums) {
        HashSet<Integer> hash = new HashSet<>();
        for (int num:nums){
            hash.add(num);
        }
        return Math.min(nums.length/2, hash.size());
    }
}