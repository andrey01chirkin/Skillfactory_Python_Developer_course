!function(){"use strict";function t(n){return t="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},t(n)}function n(t){return function(t){if(Array.isArray(t))return o(t)}(t)||function(t){if("undefined"!=typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)}(t)||r(t)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function e(t,n){return function(t){if(Array.isArray(t))return t}(t)||function(t,n){var e=null==t?null:"undefined"!=typeof Symbol&&t[Symbol.iterator]||t["@@iterator"];if(null!=e){var r,o,i=[],l=!0,a=!1;try{for(e=e.call(t);!(l=(r=e.next()).done)&&(i.push(r.value),!n||i.length!==n);l=!0);}catch(t){a=!0,o=t}finally{try{l||null==e.return||e.return()}finally{if(a)throw o}}return i}}(t,n)||r(t,n)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function r(t,n){if(t){if("string"==typeof t)return o(t,n);var e=Object.prototype.toString.call(t).slice(8,-1);return"Object"===e&&t.constructor&&(e=t.constructor.name),"Map"===e||"Set"===e?Array.from(t):"Arguments"===e||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)?o(t,n):void 0}}function o(t,n){(null==n||n>t.length)&&(n=t.length);for(var e=0,r=new Array(n);e<n;e++)r[e]=t[e];return r}function i(t,n,r){var o=document.createElement(t);return Object.entries(n||{}).forEach((function(t){var n=e(t,2),r=n[0],i=n[1];o.setAttribute(r,i)})),(r||[]).forEach((function(t){return o.appendChild(t)})),o}function l(r){var o=new FormData;function i(t,e){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:[],i=[].concat(n(r),[t]),l=i.map((function(t,n){return 0===n?t:"[".concat(t,"]")})).join("");o.append(l,e)}function l(r,o){var a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:[];if(void 0!==o){var c=t(o);"number"!==c&&"string"!==c?"boolean"!==c?Array.isArray(o)?o.forEach((function(t,e){l(e,t,[].concat(n(a),[r]))})):"object"!==c?i(r,o,a):Object.entries(o).forEach((function(t){var o=e(t,2);l(o[0],o[1],[].concat(n(a),[r]))})):i(r,o?1:0,a):i(r,o,a)}}return Object.entries(r).forEach((function(t){var n=e(t,2);l(n[0],n[1],[])})),o}function a(t){var n=new Event(t);document.dispatchEvent(n)}var c=["poll_id","client_id","location"];function u(t,n){var e=Object.keys(t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(t);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(t,n).enumerable}))),e.push.apply(e,r)}return e}function f(t){for(var n=1;n<arguments.length;n++){var e=null!=arguments[n]?arguments[n]:{};n%2?u(Object(e),!0).forEach((function(n){s(t,n,e[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(e)):u(Object(e)).forEach((function(n){Object.defineProperty(t,n,Object.getOwnPropertyDescriptor(e,n))}))}return t}function s(t,n,e){return n in t?Object.defineProperty(t,n,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[n]=e,t}function d(t,n){if(null==t)return{};var e,r,o=function(t,n){if(null==t)return{};var e,r,o={},i=Object.keys(t);for(r=0;r<i.length;r++)e=i[r],n.indexOf(e)>=0||(o[e]=t[e]);return o}(t,n);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(t);for(r=0;r<i.length;r++)e=i[r],n.indexOf(e)>=0||Object.prototype.propertyIsEnumerable.call(t,e)&&(o[e]=t[e])}return o}function p(t,n){(null==n||n>t.length)&&(n=t.length);for(var e=0,r=new Array(n);e<n;e++)r[e]=t[e];return r}function y(t){return y="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},y(t)}function m(t){return{location:document.location.href}}!function(){var t="https://foquz.ru",n=t;window.FOQUZ_SDK=window.FOQUZ_SDK||{};var e=window.FOQUZ_SDK;e._test&&(t=e._test.root||t,n=e._test.assetsRoot||t);var r,o,u,s,v=(r="".concat(n,"/widgets/poll/style.css"),new Promise((function(t){var n=document.createElement("link");n.rel="stylesheet",n.href=r,document.head.appendChild(n),n.onload=function(){t()}}))),b=null;function h(n){return new Promise((function(e){var r=l({poll_id:n.poll_id,client_id:n.client_id,location:n.location,params:d(n,c)}),o=new XMLHttpRequest;o.open("POST","".concat(t,"/foquz/default/widget-poll")),o.send(r),o.onload=function(){var t=function(t){var n=t.responseText||"",e={show:!1};try{var r=JSON.parse(n),o=JSON.parse(r),i=o.link,l=(o.params,function(t){if(!t)return"";var n=new URL(t);return n.searchParams.set("nopreview",1),n.href}(i)),a=!1;l&&"1"==new URL(l).searchParams.get("simple")&&(a=!0),e={show:!!i,pollUrl:l,isSimple:a}}catch(t){}return e}(o);e(t)}}))}function w(t,n){b&&(b.element.remove("full-view"),b.destroy());var e=t.show,r=t.pollUrl,o=t.isSimple;e&&v.then((function(){var t=function(t){var n=i("div",{class:"foquz-poll-modal__mask"}),e=i("div",{class:"foquz-poll-modal__close"}),r=i("iframe",{class:"foquz-poll-frame"}),o=i("div",{id:"foquz-poll-modal",class:"foquz-poll-modal"},[i("div",{class:"foquz-poll-modal__scroll"},[n,i("div",{class:"foquz-poll-modal__content"},[e,r,i("div",{class:"foquz-poll-modal__loader"},[i("span")])])])]),l=function(){o.classList.remove("shown"),a("foquz::hidden")},c=function(){o.classList.add("shown"),a("foquz::shown")};n.onclick=l;var u=!1,f=null;e.innerHTML="&times;",e.onclick=l;var s=function(t){o.classList.toggle("loading",t),u=!t,t||"function"!=typeof f||(f(),f=null)},d=function(t){if(t.source===r.contentWindow){var n=t.data;try{var e=JSON.parse(n);"fz:resize"===e.type&&e.height>100&&(r.height=e.height)}catch(t){}}};return window.addEventListener("message",d,!1),l(),s(!0),{element:o,frame:r,hide:function(){l()},show:function(){u||t?c():f=function(){return c()}},setPollUrl:function(t){s(!0),r.onload=function(){r.onload=null,s(!1)},r.src=t},destroy:function(){o.remove(),a("foquz::destroyed"),window.removeEventListener("message",d,!1)}}}(n);b=t,o?t.element.classList.remove("full-view"):t.element.classList.add("full-view"),document.body.appendChild(t.element),t.setPollUrl(r),t.show()}))}window.FOQUZ_SDK.openWidget=function(t){h(f(f({},t),m())).then((function(t){return w(t)}))},e.preventImmediateDisplay||h(f(f({},m()),(o=e,u=o.widget,s={},u&&"object"===y(u)&&Object.entries(u).forEach((function(t){var n,e,r=(e=2,function(t){if(Array.isArray(t))return t}(n=t)||function(t,n){var e=null==t?null:"undefined"!=typeof Symbol&&t[Symbol.iterator]||t["@@iterator"];if(null!=e){var r,o,i=[],l=!0,a=!1;try{for(e=e.call(t);!(l=(r=e.next()).done)&&(i.push(r.value),!n||i.length!==n);l=!0);}catch(t){a=!0,o=t}finally{try{l||null==e.return||e.return()}finally{if(a)throw o}}return i}}(n,e)||function(t,n){if(t){if("string"==typeof t)return p(t,n);var e=Object.prototype.toString.call(t).slice(8,-1);return"Object"===e&&t.constructor&&(e=t.constructor.name),"Map"===e||"Set"===e?Array.from(t):"Arguments"===e||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)?p(t,n):void 0}}(n,e)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()),o=r[0],i=r[1];s[o]=i})),s))).then((function(t){return w(t)})),"function"==typeof e.onLoad&&e.onLoad(),a("foquz::loaded")}()}();