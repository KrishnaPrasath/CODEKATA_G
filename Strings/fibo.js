let n = 5;

function fibonacci(n) {
  let a = 0;
  let b = 1;
  let list = [a, b];

  for (let i = 0; i < n - 2; i++) {
    temp = a + b;
    list.push(temp);
    a = b;
    b = temp;
  }

  console.log(list);
}

fibonacci(n);
