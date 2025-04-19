    document.addEventListener('DOMContentLoaded',() =>{
        const originInput = document.getElementById('id_origin');
        const destinationInput = document.getElementById('id_destination');

        const originBox = document.getElementById('origin-suggestions');
        const destinationBox = document.getElementById('destination-suggestions');

        function handlesuggestions(inputElement,type,suggestionsbox){
            inputElement.addEventListener('input',() =>{
               const query = inputElement.value;

               if (query.length > 0) {
                fetch(`/flights/suggestions/?type=${type}&q=${query}`)
                    .then(response => response.json())
                    .then(data => {
                        suggestionsbox.innerHTML = '';
                        data.results.forEach(item => {
                            const div = document.createElement('div');
                            div.textContent = item;
                            div.onclick = () => {
                                inputElement.value = item;
                                suggestionsbox.innerHTML = '';
                            };
                            suggestionsbox.appendChild(div);
                        });
                    });
               }else{
                suggestionsbox.innerHTML = '';
               }
            });

        }

        handlesuggestions(originInput,'origin',originBox)
        handlesuggestions(destinationInput,'destination',destinationBox)
    })
