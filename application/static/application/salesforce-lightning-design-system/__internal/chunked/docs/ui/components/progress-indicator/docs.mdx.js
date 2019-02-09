var SLDS=SLDS||{};SLDS["__internal/chunked/docs/ui/components/progress-indicator/docs.mdx.js"]=function(e){function t(t){for(var a,n,o=t[0],c=t[1],d=t[2],p=0,u=[];p<o.length;p++)n=o[p],r[n]&&u.push(r[n][0]),r[n]=0;for(a in c)Object.prototype.hasOwnProperty.call(c,a)&&(e[a]=c[a]);for(i&&i(t);u.length;)u.shift()();return s.push.apply(s,d||[]),l()}function l(){for(var e,t=0;t<s.length;t++){for(var l=s[t],a=!0,o=1;o<l.length;o++){var c=l[o];0!==r[c]&&(a=!1)}a&&(s.splice(t--,1),e=n(n.s=l[0]))}return e}var a={},r={23:0},s=[];function n(t){if(a[t])return a[t].exports;var l=a[t]={i:t,l:!1,exports:{}};return e[t].call(l.exports,l,l.exports,n),l.l=!0,l.exports}n.m=e,n.c=a,n.d=function(e,t,l){n.o(e,t)||Object.defineProperty(e,t,{configurable:!1,enumerable:!0,get:l})},n.r=function(e){Object.defineProperty(e,"__esModule",{value:!0})},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="/assets/scripts/bundle/";var o=this.webpackJsonpSLDS___internal_chunked_docs=this.webpackJsonpSLDS___internal_chunked_docs||[],c=o.push.bind(o);o.push=t,o=o.slice();for(var d=0;d<o.length;d++)t(o[d]);var i=c;return s.push([258,0]),l()}({0:function(e,t){e.exports=React},255:function(e,t){e.exports=".docs-codeblock-example .slds-backdrop {\n  position: absolute; }\n\n.docs-codeblock-example .slds-modal {\n  position: absolute; }\n"},256:function(e,t,l){var a=l(255);"string"==typeof a&&(a=[[e.i,a,""]]);var r={hmr:!0,transform:void 0};l(18)(a,r);a.locals&&(e.exports=a.locals)},257:function(e,t,l){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.examples=t.states=t.Step=t.Progress=void 0;var a=d(l(0)),r=d(l(1)),s=d(l(3)),n=l(29),o=l(35),c=l(34);function d(e){return e&&e.__esModule?e:{default:e}}var i=t.Progress=function(e){return a.default.createElement("div",{className:(0,r.default)("slds-progress",e.className)},a.default.createElement("ol",{className:"slds-progress__list"},e.children),a.default.createElement(c.ProgressBar,{className:"slds-progress-bar_x-small",value:e.value}))},p=t.Step=function(e){return a.default.createElement("li",{className:(0,r.default)("slds-progress__item",e.className,e.active?"slds-is-active":null,e.done?"slds-is-completed":null,e.error?"slds-has-error":null)},e.done&&!e.error?a.default.createElement(s.default,{className:"slds-button_icon slds-progress__marker slds-progress__marker_icon",symbol:"success","aria-describedby":e["aria-describedby"],assistiveText:e.done?e.children+" - Completed":null,title:e.done?e.children+" - Completed":null}):e.error?a.default.createElement(s.default,{className:"slds-button_icon slds-progress__marker slds-progress__marker_icon",symbol:"error","aria-describedby":e["aria-describedby"],assistiveText:e.error?e.children+" - Error":null,title:e.error?e.children+" - Error":null}):a.default.createElement("button",{className:"slds-button slds-progress__marker","aria-describedby":e["aria-describedby"]},a.default.createElement("span",{className:"slds-assistive-text"},e.children," ",e.active?"- Active":null)))};t.default=a.default.createElement("div",{className:"demo-only",style:{padding:"1rem"}},a.default.createElement(i,{value:"0"},a.default.createElement(p,{active:!0},"Step 1"),a.default.createElement(p,null,"Step 2"),a.default.createElement(p,null,"Step 3"),a.default.createElement(p,null,"Step 4"),a.default.createElement(p,null,"Step 5")));t.states=[{id:"next-step",label:"Next Step",element:a.default.createElement("div",{className:"demo-only",style:{padding:"1rem"}},a.default.createElement(i,{value:"25"},a.default.createElement(p,{done:!0},"Step 1"),a.default.createElement(p,{active:!0},"Step 2"),a.default.createElement(p,null,"Step 3"),a.default.createElement(p,null,"Step 4"),a.default.createElement(p,null,"Step 5")))},{id:"has-error",label:"Step - Error",element:a.default.createElement("div",{className:"demo-only",style:{padding:"1rem"}},a.default.createElement(i,{value:"25"},a.default.createElement(p,{done:!0},"Step 1"),a.default.createElement(p,{error:!0},"Step 2"),a.default.createElement(p,null,"Step 3"),a.default.createElement(p,null,"Step 4"),a.default.createElement(p,null,"Step 5")))},{id:"tooltip",label:"Tooltip",element:a.default.createElement("div",{className:"demo-only",style:{padding:"3rem 1rem 0"}},a.default.createElement(i,{value:"50"},a.default.createElement(p,{done:!0},"Step 1"),a.default.createElement(p,{done:!0},"Step 2"),a.default.createElement(p,{active:!0,"aria-describedby":"step-3-tooltip"},"Step 3"),a.default.createElement(p,null,"Step 4"),a.default.createElement(p,null,"Step 5")),a.default.createElement(n.Tooltip,{className:"slds-nubbin_bottom",id:"step-3-tooltip",style:{position:"absolute",top:"0px",left:"calc(50% + 7px)",transform:"translateX(-50%)"}},"Verify Email"))}],t.examples=[{id:"modal",label:"In a modal",element:a.default.createElement("div",{className:"demo-only",style:{height:"640px"}},a.default.createElement(o.Modal,{className:"slds-modal_large","aria-labelledby":"header43"},a.default.createElement(o.ModalHeader,null,a.default.createElement("h2",{id:"header43",className:"slds-text-heading_medium"},"Modal Header")),a.default.createElement(o.ModalContent,{className:"slds-grow slds-p-around_medium"}),a.default.createElement(o.ModalFooter,{className:"slds-grid slds-grid_align-spread"},a.default.createElement("button",{className:"slds-button slds-button_neutral"},"Cancel"),a.default.createElement(i,{className:"slds-progress_shade",value:"25"},a.default.createElement(p,{done:!0},"Step 1"),a.default.createElement(p,{active:!0},"Step 2"),a.default.createElement(p,null,"Step 3"),a.default.createElement(p,null,"Step 4"),a.default.createElement(p,null,"Step 5")),a.default.createElement("button",{className:"slds-button slds-button_brand"},"Save"))),a.default.createElement("div",{className:"slds-backdrop slds-backdrop_open"}))},{id:"shade",label:"On a gray background",element:a.default.createElement("div",{className:"demo-only",style:{background:"#F3F2F2",padding:"1rem"}},a.default.createElement(i,{className:"slds-progress_shade",value:"25"},a.default.createElement(p,{done:!0},"Step 1"),a.default.createElement(p,{active:!0},"Step 2"),a.default.createElement(p,null,"Step 3"),a.default.createElement(p,null,"Step 4"),a.default.createElement(p,null,"Step 5")))}]},258:function(e,t,l){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.getContents=t.getElement=void 0;var a=l(0),r=(E(a),l(7)),s=E(r),n=E(l(9)),o=E(l(11)),c=E(l(10)),d=E(l(12)),i=l(257),p=l(65),u=l(29),m=l(35);E(l(256));function E(e){return e&&e.__esModule?e:{default:e}}var S=r.factories.code,f=r.factories.h2,h=r.factories.h3,g=r.factories.p,v=t.getElement=function(){return(0,a.createElement)(s.default,{},(0,a.createElement)("div",{className:"doc lead"},"A progress indicator component communicates to the user the progress of a particular process."),(0,a.createElement)(c.default,{title:"Progress Indicator Base Horizontal"},(0,a.createElement)(n.default,null,(0,a.createElement)(i.Progress,{value:"0"},(0,a.createElement)(i.Step,{active:!0},"Step 1"),(0,a.createElement)(i.Step,null,"Step 2"),(0,a.createElement)(i.Step,null,"Step 3"),(0,a.createElement)(i.Step,null,"Step 4"),(0,a.createElement)(i.Step,null,"Step 5")))),f({id:"Implementation-Requirements"},"Implementation Requirements"),(0,a.createElement)(d.default,{type:"note",header:"JavaScript Requirements"},"The ",(0,a.createElement)("code",{className:"doc"},".slds-progress-bar")," accepts a range from 0% to 100%, and this percentage should be applied with inline styling to the ",(0,a.createElement)("code",{className:"doc"},"div")," with class ",(0,a.createElement)("code",{className:"doc"},"slds-progress-bar__value")," using JavaScript. If implementing a horizontal progress indicator, set the width, otherwise set the height for vertical progress indicators."),g({},(0,a.createElement)(d.default,{type:"a11y",header:"Accessibility Requirements"},"As the percentage of completion changes, be sure to update the ",(0,a.createElement)("code",{className:"doc"},"aria-valuenow")," property on the ",S({},"<div>")," with ",S({},'class="slds-progress-bar"'),", as well as the ",S({},"slds-assistive-text")," ",S({},"<span>"),".")),(0,a.createElement)(o.default,{toggleCode:!1},(0,a.createElement)("div",{className:"slds-progress-bar slds-progress-bar_x-small","aria-valuemin":"0","aria-valuemax":"100","aria-valuenow":"50",role:"progressbar"},(0,a.createElement)("span",{className:"slds-progress-bar__value",style:{width:"50%"}},(0,a.createElement)("span",{className:"slds-assistive-text"},"Progress: 50%")))),f({id:"Horizontal"},"Horizontal"),h({id:"Active-Step"},"Active Step"),g({},"When a step becomes active, the ",S({},"<div>")," with class ",S({},".slds-progress__item")," should also get the class ",S({},".slds-is-active"),"."),g({},(0,a.createElement)(d.default,{type:"a11y",header:"Accessibility Requirements"},'When a step is active, be sure to append "- Active" to the hidden button text in the ',S({},"<span>")," with class ",S({},"slds-assistive-text"),", such as ",S({},"Step 1 - Active"),".")),(0,a.createElement)(c.default,{title:"Progress Indicator Active Horizontal"},(0,a.createElement)(n.default,null,(0,a.createElement)(i.Progress,{value:"0"},(0,a.createElement)(i.Step,{active:!0},"Step 1"),(0,a.createElement)(i.Step,null,"Step 2"),(0,a.createElement)(i.Step,null,"Step 3"),(0,a.createElement)(i.Step,null,"Step 4"),(0,a.createElement)(i.Step,null,"Step 5")))),h({id:"Completed-Step"},"Completed Step"),g({},"When the step is completed, the ",S({},".slds-is-active")," class should be replaced with the class ",S({},".slds-is-completed")," on ",S({},".slds-progress__item"),". At that point, the ",S({},".slds-progress__item"),' element will receive a "success" icon, providing feedback that the step has been completed.'),g({},(0,a.createElement)(d.default,{type:"a11y",header:"Accessibility Requirements"},'When a step is completed, be sure to append "- Completed" to the hidden button text in the ',S({},"<span>")," with class ",S({},"slds-assistive-text"),", such as ",S({},"Step 2 - Completed"),".")),(0,a.createElement)(c.default,{title:"Progress Indicator Done Horizontal"},(0,a.createElement)(n.default,null,(0,a.createElement)(i.Progress,{value:"50"},(0,a.createElement)(i.Step,{done:!0},"Step 1"),(0,a.createElement)(i.Step,{done:!0},"Step 2"),(0,a.createElement)(i.Step,{active:!0},"Step 3"),(0,a.createElement)(i.Step,null,"Step 4"),(0,a.createElement)(i.Step,null,"Step 5")))),h({id:"Error-in-a-Step"},"Error in a Step"),g({},"When an error has occurred on a step, the ",S({},"<div>")," with class ",S({},".slds-progress__item")," should also get the class ",S({},".slds-has-error"),"."),g({},(0,a.createElement)(d.default,{type:"a11y",header:"Accessibility Requirements"},'When a step has an error, be sure to append "- Error" to the hidden button text in the ',S({},"<span>")," with class ",S({},"slds-assistive-text"),", such as ",S({},"Step 3 - Error"),".")),(0,a.createElement)(c.default,{title:"Progress Indicator Done Horizontal"},(0,a.createElement)(n.default,null,(0,a.createElement)(i.Progress,{value:"50"},(0,a.createElement)(i.Step,{done:!0},"Step 1"),(0,a.createElement)(i.Step,{done:!0},"Step 2"),(0,a.createElement)(i.Step,{error:!0},"Step 3"),(0,a.createElement)(i.Step,null,"Step 4"),(0,a.createElement)(i.Step,null,"Step 5")))),h({id:"Step-Title-Tooltip"},"Step Title Tooltip"),(0,a.createElement)(d.default,{type:"a11y",header:"Accessibility Requirements"},"When a step's tooltip is visible, the step's button needs the ",(0,a.createElement)("code",{className:"doc"},"aria-describedby")," attribute, whose value should be the ",(0,a.createElement)("code",{className:"doc"},"id")," of the associated tooltip."),(0,a.createElement)(c.default,{title:"Progress Indicator Tooltip Horizontal"},(0,a.createElement)(n.default,null,(0,a.createElement)("div",{style:{padding:"3.5rem 1rem 0"}},(0,a.createElement)(i.Progress,{value:"50"},(0,a.createElement)(i.Step,{done:!0},"Step 1"),(0,a.createElement)(i.Step,{done:!0},"Step 2"),(0,a.createElement)(i.Step,{active:!0,"aria-describedby":"step-3-tooltip"},"Step 3"),(0,a.createElement)(i.Step,null,"Step 4"),(0,a.createElement)(i.Step,null,"Step 5")),(0,a.createElement)(u.Tooltip,{className:"slds-nubbin_bottom",id:"step-3-tooltip",style:{position:"absolute",top:"1rem",left:"calc(50% + 6px)",transform:"translateX(-50%)"}},"Verify Email")))),h({id:"In-a-Modal"},"In a Modal"),(0,a.createElement)(c.default,{title:"Progress Indicator Horizontal in Modal"},(0,a.createElement)(n.default,{style:{height:"640px"}},(0,a.createElement)("div",null,(0,a.createElement)(m.Modal,{className:"slds-modal_large","aria-labelledby":"header43"},(0,a.createElement)(m.ModalHeader,null,(0,a.createElement)("h2",{id:"header43",className:"slds-text-heading_medium"},"Modal Header")),(0,a.createElement)(m.ModalContent,{className:"slds-grow slds-p-around_medium"}),(0,a.createElement)(m.ModalFooter,{className:"slds-grid slds-grid_align-spread"},(0,a.createElement)("button",{className:"slds-button slds-button_neutral"},"Cancel"),(0,a.createElement)(i.Progress,{className:"slds-progress_shade",value:"25"},(0,a.createElement)(i.Step,{done:!0},"Step 1"),(0,a.createElement)(i.Step,{active:!0},"Step 2"),(0,a.createElement)(i.Step,null,"Step 3"),(0,a.createElement)(i.Step,null,"Step 4"),(0,a.createElement)(i.Step,null,"Step 5")),(0,a.createElement)("button",{className:"slds-button slds-button_brand"},"Save"))),(0,a.createElement)("div",{className:"slds-backdrop slds-backdrop_open"})))),h({id:"On-a-Gray-Background"},"On a Gray Background"),(0,a.createElement)(c.default,{title:"Progress Indicator Horizontal Gray Background"},(0,a.createElement)(n.default,{style:{background:"#F3F2F2",padding:"1rem"}},(0,a.createElement)(i.Progress,{className:"slds-progress_shade",value:"25"},(0,a.createElement)(i.Step,{done:!0},"Step 1"),(0,a.createElement)(i.Step,{active:!0},"Step 2"),(0,a.createElement)(i.Step,null,"Step 3"),(0,a.createElement)(i.Step,null,"Step 4"),(0,a.createElement)(i.Step,null,"Step 5")))),f({id:"Vertical"},"Vertical"),g({},"To display a vertical progress indicator, the ",S({},"<div>")," with class ",S({},".slds-progress")," should also get the class ",S({},".slds-progress_vertical"),". The vertical progress indicator will take up 100% of the height of its container. The step titles in the vertical variant appear next to the step, instead of in a tooltip."),g({},(0,a.createElement)(d.default,{type:"note",header:"Implementation Note"},"The key markup difference between the horizontal and vertical variants is the progress markers. Horizontal progress indicators use ",S({},"<button>")," for each step, whereas Vertical progress indicator steps are not interactive and therefore simply use ",S({},"<div>"),".")),(0,a.createElement)(c.default,{title:"Progress Indicator Vertical"},(0,a.createElement)(n.default,null,(0,a.createElement)(p.Progress,{value:"25"},(0,a.createElement)(p.Step,{done:!0},"Step 1"),(0,a.createElement)(p.Step,{active:!0},"Step 2"),(0,a.createElement)(p.Step,null,"Step 3"),(0,a.createElement)(p.Step,null,"Step 4"),(0,a.createElement)(p.Step,null,"Step 5")))),h({id:"Green-Success"},"Green Success"),g({},"To create a green completed step, the ",S({},".slds-progress__item")," element should also receive the ",S({},".slds-is-completed")," class. In addition, the ",S({},"<span>")," with class ",S({},".slds-progress__marker_icon")," should also get the class ",S({},"slds-progress__marker_icon-success"),"."),(0,a.createElement)(c.default,{title:"Progress Indicator Vertical Success"},(0,a.createElement)(n.default,null,(0,a.createElement)(p.Progress,{value:"25"},(0,a.createElement)(p.Step,{done:!0,hasSuccessMarker:!0},"Step 1"),(0,a.createElement)(p.Step,{active:!0},"Step 2"),(0,a.createElement)(p.Step,null,"Step 3"),(0,a.createElement)(p.Step,null,"Step 4"),(0,a.createElement)(p.Step,null,"Step 5")))),h({id:"Error-in-a-Step-2"},"Error in a Step"),g({},"When an error has occurred on a step, the ",S({},"<div>")," with class ",S({},".slds-progress__item")," should also get the class ",S({},".slds-has-error"),"."),(0,a.createElement)(c.default,{title:"Progress Indicator Vertical Success"},(0,a.createElement)(n.default,null,(0,a.createElement)(p.Progress,{value:"25"},(0,a.createElement)(p.Step,{done:!0},"Step 1"),(0,a.createElement)(p.Step,{error:!0},"Step 2"),(0,a.createElement)(p.Step,null,"Step 3"),(0,a.createElement)(p.Step,null,"Step 4"),(0,a.createElement)(p.Step,null,"Step 5")))),h({id:"Multiline-Step-Titles"},"Multiline Step Titles"),g({},"The vertical progress indicator also supports multiline step descriptions."),(0,a.createElement)(c.default,{title:"Progress Indicator Vertical"},(0,a.createElement)(n.default,null,(0,a.createElement)(p.Progress,{value:"25"},(0,a.createElement)(p.Step,{done:!0},"Step 1"),(0,a.createElement)(p.Step,{active:!0},"Step 2"),(0,a.createElement)(p.Step,null,"Step 3: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."),(0,a.createElement)(p.Step,null,"Step 4"),(0,a.createElement)(p.Step,null,"Step 5")))))};t.getContents=function(){return(0,r.createTableOfContents)(v())}},6:function(e,t){e.exports=JSBeautify}});