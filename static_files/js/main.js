function randomized_queens(n){
	let res = [], temp = new Array(n)
	backtrack(res, temp, false, 0)
	return res[0]
}

function backtrack(res, temp, flip_switch, idx){
	if (temp.length == idx){
		res.push(temp.slice(0))
		flip_switch = true 
		return
	}
	for(let i = 0; i < temp.length; i++){
		temp[idx] = Math.floor(Math.random() * temp.length)
		if (valid_position(temp, idx)){
			backtrack(res, temp, flip_switch, idx + 1)
		}
		if (flip_switch == true) { break }
	}
}

function valid_position(temp, idx){
	for(let i = 0; i < idx; i++){
		if (temp[i] == temp[idx] ||
			Math.abs(temp[i] - temp[idx]) == Math.abs(idx - i)){
				return false 
			}
	}
	return true 
}

let generate_queens = document.querySelector('.queens-generator')
let rows = document.querySelectorAll('.row')
let queen_position = null 
let queens = []

function clear_board(arr){
	for(let i = 0; i < arr.length; i++){
		queen_position = arr[i]
		rows[i].children[queen_position].innerHTML = ''
	}
}

function place_queens(queens){
	for(let i = 0; i < queens.length; i++){
		queen_position = queens[i]
		rows[i].children[queen_position].innerHTML = '&#9813'
	}
}

if (generate_queens){
	generate_queens.addEventListener('click', function(e){
		e.preventDefault()
		clear_board(queens)
		queens = randomized_queens(8)
		place_queens(queens)
	})
}