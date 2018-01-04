import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.lang.Math;

class KnightPuzzle {
	/**
	 * Prototype of the KnightPuzzle from uk.org.ird.the-puzzle-returns
	 * This class generates a 8x8 array of letters and a start point 'N'
	 * in which a random word can be spelt out by legal chess moves for a 
	 * knight.
	 */
	 public static List<Character> generate(String wordlist) {
	 	 List<Character> puzzle;
	 	 
	 	 // Randomly select a word from the word list
	 	 
	 	 String word = "NAZDO";
	 	 
	 	 while(true) {
	 	 	 puzzle = Arrays.asList(new Character[64]);
	 	 	 int pos = (int)(Math.random()*63);
	 	 	 // Randomly select a start point and enter the first letter
	 	 	 puzzle.set(pos, word.charAt(0));
	 	 	 // For each subsequent letter; work out all possible next positions (max 8),
	 	 	 // select one at random and place a letter
	 	 	 List<Integer> nextMoves = null;
	 	 	 for(int i=1; i<word.length(); i++) {
	 	 	 	 nextMoves = possibleKnightPositions(pos, puzzle);
	 	 	 	 if(nextMoves.size() == 0)
	 	 	 	 	 break;
	 	 	 	 pos = choose(nextMoves);
	 	 	 	 puzzle.set(pos, word.charAt(i));
	 	 	 }
	 	 	 if(nextMoves.size() == 0)
	 	 	 	 continue;
	 	 	 break;
	 	 }

	 	 
	 	 // From a specified charset, enter random letters into all other empty grids
	 	 
	 	 return puzzle;
	 }
	 
	 public static List<Integer> possibleKnightPositions(int startPos, List<Character> grid) {
	 	 ArrayList<Integer> res = new ArrayList<>();
	 	 List<Integer> relPos = Arrays.asList(-17, -15, -10, -6, 6, 10, 15, 17);
	 	 for(int adjustment : relPos){
	 	 	 int pos = startPos + adjustment;
	 	 	 if(pos >= 0 && pos < 64 && grid.get(pos) == null)
	 	 	 	 res.add(pos);
	 	 }
	 	 System.out.println("Possible positions from startPos=" + startPos + " : " + res);
	 	 return res;
	 }
	 
	 public static int choose(List<Integer> L) {
	 	 return L.get((int)(Math.random()*L.size()));
	 }
	 
	 public static void main(String[] args) {
	 	 System.out.println(generate(""));
	 }
}