package Level_2;

import java.util.*;
//https://school.programmers.co.kr/learn/courses/30/lessons/84512
public class VowelDictionary {

    public int solution(String word) {

        String[] vowels = {"A", "E", "I", "O", "U"};
        class BFS {
            public int index = 0;
            public int answer = 0;
            public void bfs(String targetWord, String currentWord) {
                if (answer != 0) return;
                if (targetWord.equals(currentWord)) {
                    answer = index;
                    return;
                }
                if (currentWord.length() == 5) return;
                for (String v: vowels) {
                    index += 1;
                    bfs(targetWord, currentWord.concat(v));

                }
            }
        }
        BFS b = new BFS();
        b.bfs(word, "");

        return b.answer;
    }

}
