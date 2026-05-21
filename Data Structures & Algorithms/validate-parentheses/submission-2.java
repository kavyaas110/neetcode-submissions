class Solution {
    public boolean isValid(String s) {
        if(s.length()%2 != 0){
            return false;
        }
        else{
            Stack<Character> myStack = new Stack();
            Set<Character> open = Set.of('(','[','{');
            Set<Character> close = Set.of(')','}',']');
            Map<Character,Character> my_map = new HashMap();
            my_map.put(')','(');
            my_map.put('}','{');
            my_map.put(']','[');

            for(int i = 0; i<s.length();i++){
                Character ch = s.charAt(i);
                if(close.contains(ch)){
                    if(myStack.empty()) return false;
                    Character val = myStack.pop();
                    if (val != my_map.get(ch)) return false;
                }
                else{
                    myStack.push(ch);
                }
            }
            if(myStack.empty()) return true;
            else return false;
        }
    }
}
