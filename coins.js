/*
https://www.youtube.com/watch?v=HWW-jA6YjHk&t=980s

Goal of Question: Create a function that will give you thin minumum amount of coins needed to fill a request
Constraints: Cannot assume that given coin will be present
Given: list of coins avaliable
Outcome: return the number of coinds needed

Given: 31 cents, [25 cents,10 cents,1 cent] --> 4 coins (10 cents, 10 cents, 10 cents, 1 cent)
Given: 31 cents [25 cents, 10 cents, 5 cents, 1 cent] --> 3 coins (25 cents, 5 cents, 1 cent)
Given: 75 cents [10 cents, 5 cents, 1 cent] --> 8 coins (10 cents, 10 cents, 10 cents, 10 cents, 10 cents, 10 cents, 10 cents, 5 cents)
*/

function min_coins(change,avaliable){
  let map = [[0,change]]

  while(map.length > 0){
    let current = map.sort((a,b) => a[0] - b[0]).shift()

    if(current[1] == 0)
      return current[0]

    avaliable.forEach(coin =>{
      if(current[1] - coin >= 0){
        let min_coins = Math.floor(current[1] / coin)
        map.push([current[0] + min_coins, current[1] - (coin * min_coins)])
      }
    })
  }
}
console.log(min_coins(31,[25,10,1]))
console.log(min_coins(31,[25,5,10,1]))
console.log(min_coins(75,[5,10,1]))
