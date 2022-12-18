package Level_3;
//https://school.programmers.co.kr/learn/courses/30/lessons/43105

public class IntegerTriangle {
    public int solution(int[][] triangle) {
        if (triangle.length == 1) {
            return triangle[0][0];
        }
        for (int i = triangle.length-2; i >= 0; i--) {
            int[] prevRow = triangle[i+1];
            for (int j = 0; j < triangle[i].length; j++) {
                triangle[i][j] += Math.max(prevRow[j], prevRow[j+1]);
            }
        }

        return triangle[0][0];
    }
}
