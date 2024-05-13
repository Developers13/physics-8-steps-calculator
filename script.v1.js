
const p = document.querySelector("#prompt");
const ph = document.querySelector("#phead");
const pc = document.querySelector("#pcontent");
const submit = document.querySelector("#submit");
addEventListener("mpy:ready", function () {
  document
    .querySelector("#submit")
    .setAttribute(
      "class",
      "cursor-pointer bg-transparent hover:bg-blue-500 hover:scale-110 bg-opacity-30  rounded-full  px-2  py-1  my-2   transition "
    );
  p.setAttribute(
    "class",
    "bg-green-500  bg-opacity-50 my-4  mx-3  p-2 rounded-sm  shadow-sm "
  );
  ph.innerText = "You are all set!";
  pc.innerText = "PyScript is ready.You are ready to go!";
  submit.setAttribute(
    "class",
    "cursor-pointer bg-blue-300  rounded-full px-2 py-1 my-2 transition"
  )
});
//Clear button

  document.querySelector("#clear").addEventListener("click", function () {
    document.querySelector("#input").value = "";
  });

//Processing transition


submit.addEventListener("click", function () {
  submit.setAttribute(
    "class",
    "cursor-progress bg-indigo-300  rounded-full px-2 py-1 my-2 transition"
  );

  setTimeout(() => (submit.innerText = "Processing..."), 500);
});
addEventListener("mpy:done", function () {
  submit.setAttribute(
    "class",
    "cursor-pointer bg-blue-300  rounded-full px-2 py-1 my-2 transition"
  )
});

//test
