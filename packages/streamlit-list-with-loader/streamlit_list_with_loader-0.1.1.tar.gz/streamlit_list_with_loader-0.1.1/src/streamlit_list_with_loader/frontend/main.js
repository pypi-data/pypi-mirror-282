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
    const { data } = event.detail.args;

    const nameElement = document.getElementById("name")

    nameElement.innerText = data.name

    const statusElement = document.getElementById("status")
    
    statusElement.innerHTML = data.status === 'loading' ? '<div class="loader"></div>' : '<div style="margin: 0.85rem">❌</div>'

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
Streamlit.setFrameHeight(50)
