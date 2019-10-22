#include <iostream>
#include <math.h>
#include <vector>
using namespace std;
//https://www.youtube.com/watch?v=xC8CGv1CyFk
//Section 1 : Given a list of coins and your position, find the closest coin to you
//Section 2: Given a list of coins, your position, and enemies positions, find the closest coin that you can get before an enemy gets
class Point{
  public:
    Point(){}
    Point(int x1,int y1){
      x = x1;
      y = y1;
    }
    int x,y;
};
class Node{
  public:
  Point closest;
  double score = INFINITY;
};

double manhattan(Point item1,Point item2){
  return abs(item1.x - item2.x) + abs(item1.y - item2.y);
}
Node get_closest(Point user,vector<Point> coins){
  Node closest;
  double score;
  for(Point coin:coins){
    if((score = manhattan(coin,user))  < closest.score){
      closest.score = score;
      closest.closest = coin;
    }
  }
  return closest;
}


int main(){
  vector<Point> coins {Point(1,5),Point(5,1),Point(2,2)};
  Point user(4,2);
  //Section 1
  Node n = get_closest(user,coins);
  //Section 2
  Node n2;
  double score;
  vector<Point> enemies {Point(5,1),Point(1,5)};
  for(Point coin:coins){
    if((score = manhattan(user,coin)) < n2.score && get_closest(coin,enemies).score > n2.score){
      n2.score = score;
      n2.closest = coin;
    }
  }
  cout<<n.closest.x<<"   "<<n.closest.y<<"   "<<n.score<<endl;
  cout<<n2.closest.x<<"   "<<n2.closest.y<<endl;
  return 1;
}
