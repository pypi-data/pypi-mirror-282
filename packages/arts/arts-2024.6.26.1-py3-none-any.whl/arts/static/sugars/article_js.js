let show = (src) => {event.preventDefault(); window.open(src, '_blank')}

let video_template = `<div><video loading="lazy" controls onclick="show('{{src}}')"><source src='{{src}}' type='video/mp4'></video></div>`
let img_template = `<div><img loading="lazy" src='{{src}}' onclick="show('{{src}}')"></div>`

let big_video_template = `<video loading="lazy" controls onclick="show('{{src}}')"><source src='{{src}}' type='video/mp4'></video>`
let big_img_template = `<img loading="lazy" src='{{src}}' onclick="show('{{src}}')">`

let go_home = `\n\n<button class="go_home" onclick="show('https://lcctoor.github.io/arts')">[作者主页]</button> 👈`

let is_web = document.URL.startsWith('http')
if (is_web) {window.my_host = document.URL.replace(/github.io\/arts\//g, "github.io/arts_static1/").replace(/\/$/, '') + '/'}

let creat_media = (media) => {
    if (media) {
        let content = []
        let video_suffixes = ['mp4']
        let img_suffixes = ['jpg', 'png', 'jpeg']
        for (let src of media) {
            let suffix = src.match(/\.([^.]+)$/)
            if (is_web && src.startsWith('oas1_')) {src = my_host + src}
            if (suffix) {
                if (video_suffixes.includes(suffix[1]))
                    {content.push(video_template.replace(/{{src}}/g, src))}
                else if (img_suffixes.includes(suffix[1]))
                    {content.push(img_template.replace(/{{src}}/g, src))}
            }
        }
        let ch_15 = document.createElement('div')
        ch_15.classList.add('ch_15')
        ch_15.innerHTML += content.join('\n')
        document.body.getElementsByTagName('pre')[0].insertBefore(ch_15, document.currentScript)
    }
}

let creat_big_media = (media) => {
    if (media) {
        let content = []
        let video_suffixes = ['mp4']
        let img_suffixes = ['jpg', 'png', 'jpeg']
        for (let src of media) {
            let suffix = src.match(/\.([^.]+)$/)
            if (is_web && src.startsWith('oas1_')) {src = my_host + src}
            if (suffix) {
                if (video_suffixes.includes(suffix[1]))
                    {content.push(big_video_template.replace(/{{src}}/g, src))}
                else if (img_suffixes.includes(suffix[1]))
                    {content.push(big_img_template.replace(/{{src}}/g, src))}
            }
        }
        let ch_16 = document.createElement('div')
        ch_16.classList.add('ch_16')
        ch_16.innerHTML += content.join('\n')
        document.body.getElementsByTagName('pre')[0].insertBefore(ch_16, document.currentScript)
    }
}

let clean_text = (text) => text.replace(/\s+$/, '').replace(/[\s\\]*\\[\s\\]*/g, '')

let render = (author=true) => {
    document.title = decodeURIComponent(document.URL).match(/\/(\d*\s*-\s*)?([^/\\]+)\/?$/)[2]
    let pre = document.body.getElementsByTagName('pre')[0]
    if (author) {
        pre.innerHTML = clean_text(pre.innerHTML) + go_home
    }
    else {
        pre.innerHTML = clean_text(pre.innerHTML)
    }
    pre.addEventListener('dblclick', () => {window.open(document.URL, '_blank')})
}