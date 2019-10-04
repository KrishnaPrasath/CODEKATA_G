let num = Math.floor(1000 + Math.random() * 9000);

console.log(num);
function checkDuplicate(num) {
  let digits = [];
  let result = {};
  while (num > 0) {
    digits.push(num % 10);
    num = Math.floor(num / 10);
  }

  for (let i = 0; i < 4; i++) {
    result[digits[i]] = "exist";
  }
  let size = Object.keys(result).length;
  if (size == 4) return true;
  else return false;
}

if (checkDuplicate(num)) console.log("Unique");
else console.log("has duplicates");
