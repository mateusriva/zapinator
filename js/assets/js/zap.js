$(function() {
  $("#strength-slider").on("input change", e => {
    const zapStrength = e.target.value
    
    const emojiArray = [
      "crazy",
      "surprised",
      "sunglasses",
      "muscle",
      "lol",
      "okay",
      "okay",
      "top",
    ]
    const zapEmojisPerStrength = [1, 2, 3, 4, 8]
    const strengthTitleArray = [
      "Zap força fraca",
      "Zap força média",
      "Isso que é zap bb",
      "Zap monstrão",
      "Zap topper d+"
    ]

    const finalZap = `
      <div class="mb10">${strengthTitleArray[zapStrength]}</div>
      ${emojiArray.slice(0, zapEmojisPerStrength[zapStrength]).map(
        emoji => `<img class="emoji" src="images/emojis/${emoji}.png" alt="${emoji}"/>`
      ).join(" ")}
    `

    $("#strength-show").html(finalZap)
  })

  $(".mood-button").on("click", function() {
    $(".mood-button").removeClass("active")
    $(this).addClass("active")
  })
})