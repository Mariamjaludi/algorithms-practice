var numJewelsInStones = function(J, S) {
    let i = S.length - 1;
    let count = 0
    while (i >= 0) {
        if (J.indexOf(S[i]) > -1)
        {
            count++;
        }
        i--;
    }
    return count;

};
