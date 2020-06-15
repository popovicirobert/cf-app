#!/bin/bash

task_id=$1
contest_path=$2

cat << EOF> $contest_path
#include <bits/stdc++.h>
#define lsb(x) (x & (-x))
#define ll long long
#define ull unsigned long long
#define Test(tt) cout << "Case #" << tt << ": "

using namespace std;


int main() {
#ifdef HOME
    ifstream cin("$1.in");
    ofstream cout("$1.out");
#endif
    int ;
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
	
		

    return 0;
}
EOF
