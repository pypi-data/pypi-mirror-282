// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

function sendValue(value) {
  Streamlit.setComponentValue(value)
}

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event) {
  // Only run the render code the first time the component is loaded.
  if (!window.rendered) {
    // You most likely want to get the data passed in like this
    // const {input1, input2, input3} = event.detail.args

    const { data, onClick } = event.detail.args;

    const rootElement = document.getElementById("root")

    for (let i = 0; i < data.length; i++) {
      const list = document.createElement('div');

      if (data[i].status === 'loading') {
        list.innerHTML =
        `
          <div class='container'>
            <p class='name'>${data[i].name}<p/>
            <div class="loader"></div>
          </div>
        `
      } else if (data[i].status === 'failed') {
        list.innerHTML =
        `
          <div class='container'>
            <p class='name'>${data[i].name}<p/>
            <div style='margin: 0.85rem'>❌</div>
          </div>
        `
      }

      rootElement.appendChild(list)
    }

    // You'll most likely want to pass some data back to Python like this
    // sendValue({output1: "foo", output2: "bar"})
    window.rendered = true
  }
}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
Streamlit.setFrameHeight(100)
