import std.stdio;


bool bingo(int t, int[3][3] board) {

    foreach(i; 0..3) {
        if(board[i] == [t, t, t]) {
            return true;
        }
        if(
            board[0][i] == t &&
            board[1][i] == t &&
            board[2][i] == t) {
            return true;
        }
    }

    if(
        board[0][0] == t &&
        board[1][1] == t &&
        board[2][2] == t) {
        return true;
    }
    if(
        board[0][2] == t &&
        board[1][1] == t &&
        board[2][0] == t) {
        return true;
    }

    return false;
}

bool full(int[3][3] board) {
    
    foreach(i; 0..3) {
        foreach(j; 0..3) {
            if(!board[i][j]) {
                return false;
            }
        }
    }

    return true;
}

int win(int t, int[3][3] boardpre) {

    int e = 3 - t;

    if(bingo(t, boardpre)) {
        return 2;
    }
    if(bingo(e, boardpre)) {
        return 0;
    }
    if(full(boardpre)) {
        return 1;
    }

    int[3][3] boardnew;
    int r;
    bool draw = false;
    foreach(i; 0..3) {
        foreach(j; 0..3) {
            if(!boardpre[i][j]) {
                boardnew = boardpre.dup;
                boardnew[i][j] = t;
                r = win(e, boardnew);
                if(!r) {
                    return 2;
                }
                if(r == 1) {
                    draw = true;
                }
            }
        }
    }

    return draw ? 1 : 0;
}

void main() {

    int[3][3] boardinit;
    int u, cnt;
    foreach(i; 0..3) {
        foreach(j; 0..3) {
            scanf("%d", &u);
            if(u == 1) cnt++;
            if(u == 2) cnt--;
            boardinit[i][j] = u;
        }
    }

    writeln("LDW"[win(cnt ? 2 : 1, boardinit)]);
}
