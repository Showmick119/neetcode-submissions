class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> grouped = new ArrayList<List<String>>();
        Map<String, String> sortedStrs = new HashMap<>();
        List<String> used = new ArrayList<>();
        for (String str : strs) {
            char[] strChar = str.toCharArray();
            Arrays.sort(strChar);
            String sortedStr = new String(strChar);
            sortedStrs.put(str, sortedStr);
        }
        for (Map.Entry<String, String> entry : sortedStrs.entrySet()) {
            String curr = entry.getKey();
            String sortedCurr = entry.getValue();
            List<String> temp = new ArrayList<>(); // unique to each entry
            if (used.contains(curr)) {
                continue;
            }
            temp.add(curr);
            for (Map.Entry<String, String> check : sortedStrs.entrySet()) {
                String compare = check.getKey();
                String sortedCompare = check.getValue();
                if (sortedCurr.equals(sortedCompare) && !curr.equals(compare)) {
                    if (!used.contains(compare)) {
                        temp.add(compare);
                        used.add(compare);
                        used.add(curr);
                    }
                }
            }
            grouped.add(temp);
        }
        return grouped;
    }
}
