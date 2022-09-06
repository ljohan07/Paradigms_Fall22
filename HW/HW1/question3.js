function computeEnumeration(termPositions) {
    var ans = Array(termPositions);
    for (let i = 0; i < termPositions.length; i++) {
        ans[i] = enumerate(termPositions[i]);
    }
    return ans;
}
function enumerate(num) {

    if (num < 1) {
        return null;
    }
    
    var row = 0;
    var col = 0;

    // array of which positions in the array have been visited
    var visited = Array(num);
    for (let i = 0; i < num; i++) {
        visited[i] = Array(num);
        for (let j = 0; j < num; j++) {
            visited[i][j] = 0;
        }
    }

    for (let count = 1; count < num; count++) {
        visited[row][col] = 1;
        // at visited[0][0] need to move right
        if (row == 0 && col == 0) {
            row += 1;
        }
        // determine if we need to move right or move down and left
        else if (row == 0) {
            if (visited[row+1][col-1] == 1) {
                col += 1;
            }
            else {
                row += 1;
                col -= 1;
            }
        }
        // determine if we need to move down or up and right
        else if (col == 0) {
            if (visited[row-1][col+1] == 1) {
                row += 1;
            }
            else {
                row -= 1;
                col += 1;
            }
        }
        // determine if we move down/left or up/right
        else {
            if (visited[row-1][col+1] == 1) {
                row += 1;
                col -= 1;
            }
            else {
                row -= 1;
                col += 1;
            }
        }
    }
    // calculate fraction based on position
    var top = 2*(col + 1);
    var bot = 2*(row + 1);
    return `${top}/${bot}`;
}

// console.log(computeEnumeration( [1, 15, 8, 2]))
// console.log(computeEnumeration([3, 6, -1, 108]))


