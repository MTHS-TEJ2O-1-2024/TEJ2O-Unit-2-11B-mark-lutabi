/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Mark.lutabi
 * Created on: October, 2014
 * This program generates 2 random numbers
*/
// variables

let randomNumberOne: number = 0
let randomNumberTwo: number = 0

basic.clearScreen()
basic.showIcon(IconNames.Happy)

// Display the first number
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    randomNumberOne = randint(0,99)
    basic.showString('#1:'+ randomNumberOne)
    basic.showIcon(IconNames.Happy)
})

// Display the second number
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    randomNumberOne = randint(0, 99)
    basic.showString('#2:' + randomNumberTwo)
    basic.showIcon(IconNames.Happy)
})

// Shake
input.onGesture(Gesture.Shake, function () {
basic.clearScreen()
 if ( randomNumberOne < randomNumberTwo){
basic.showString(randomNumberOne + '<' + randomNumberTwo)
 }
 else{
basic.showString(randomNumberTwo + '>' + randomNumberOne)
 }
})


