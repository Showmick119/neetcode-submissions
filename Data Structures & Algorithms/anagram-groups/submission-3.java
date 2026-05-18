class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> grouped = new ArrayList<List<String>>();
        List<String> sortedStrs = new ArrayList<>();
        List<String> used = new ArrayList<>();
        for (String str : strs) {
            char[] strChar = str.toCharArray();
            Arrays.sort(strChar);
            String sortedStr = new String(strChar);
            sortedStrs.add(sortedStr); // going at the same index
        }
        for (int i = 0; i < strs.length; i++) {
            List<String> temp = new ArrayList<>();
            String curr = strs[i];
            if (used.contains(curr)) {
                continue;
            }
            temp.add(curr);
            used.add(curr);
            String sortedCurr = sortedStrs.get(i);
            for (int j = i + 1; j < strs.length; j++) {
                if (sortedCurr.equals(sortedStrs.get(j)) && !used.contains(strs[j])) {
                    temp.add(strs[j]);
                    used.add(strs[j]);
                }
            }
            grouped.add(temp);
        }
        return grouped;
    }
}