var SLDS=SLDS||{};SLDS["__internal/chunked/showcase/ui/components/tree-grid/base/example.jsx.js"]=function(e){function l(l){for(var n,d,s=l[0],o=l[1],r=l[2],u=0,m=[];u<s.length;u++)d=s[u],a[d]&&m.push(a[d][0]),a[d]=0;for(n in o)Object.prototype.hasOwnProperty.call(o,n)&&(e[n]=o[n]);for(c&&c(l);m.length;)m.shift()();return i.push.apply(i,r||[]),t()}function t(){for(var e,l=0;l<i.length;l++){for(var t=i[l],n=!0,s=1;s<t.length;s++){var o=t[s];0!==a[o]&&(n=!1)}n&&(i.splice(l--,1),e=d(d.s=t[0]))}return e}var n={},a={148:0,7:0,8:0,15:0,16:0,22:0,32:0,38:0,42:0,45:0,54:0,58:0,59:0,63:0,64:0,67:0,71:0,75:0,77:0,80:0,84:0,87:0,88:0,93:0,99:0,100:0,104:0,106:0,114:0,117:0,118:0,122:0,124:0,125:0,126:0,127:0,128:0,129:0,133:0,138:0,144:0,152:0,163:0,167:0,170:0,171:0,178:0,181:0,182:0},i=[];function d(l){if(n[l])return n[l].exports;var t=n[l]={i:l,l:!1,exports:{}};return e[l].call(t.exports,t,t.exports,d),t.l=!0,t.exports}d.m=e,d.c=n,d.d=function(e,l,t){d.o(e,l)||Object.defineProperty(e,l,{configurable:!1,enumerable:!0,get:t})},d.r=function(e){Object.defineProperty(e,"__esModule",{value:!0})},d.n=function(e){var l=e&&e.__esModule?function(){return e.default}:function(){return e};return d.d(l,"a",l),l},d.o=function(e,l){return Object.prototype.hasOwnProperty.call(e,l)},d.p="/assets/scripts/bundle/";var s=this.webpackJsonpSLDS___internal_chunked_showcase=this.webpackJsonpSLDS___internal_chunked_showcase||[],o=s.push.bind(s);s.push=l,s=s.slice();for(var r=0;r<s.length;r++)l(s[r]);var c=o;return i.push([222,0]),t()}({0:function(e,l){e.exports=React},221:function(e,l,t){"use strict";Object.defineProperty(l,"__esModule",{value:!0}),l.TreeGrid=void 0;var n=d(t(0)),a=d(t(3)),i=t(13);function d(e){return e&&e.__esModule?e:{default:e}}(l.TreeGrid=function(e){return n.default.createElement(i.Table,{hasHiddenHeader:e.hasHiddenHeader,isBordered:e.isBordered,isEditable:!0,isFixedLayout:e.isFixedLayout,isResizable:e.isResizable,selectionType:e.selectionType,type:"treegrid"},e.children)}).propTypes={children:a.default.node,hasHiddenHeader:a.default.bool,isBordered:a.default.bool,isFixedLayout:a.default.bool,isResizable:a.default.bool,selectionType:a.default.string}},222:function(e,l,t){"use strict";Object.defineProperty(l,"__esModule",{value:!0}),l.examples=l.states=l.HeadlessRows=l.DeepNestingRows=l.ExpandedRow=l.DefaultRows=l.HeadlessRow=l.Row=void 0;var n=r(t(0)),a=r(t(1)),i=r(t(3)),d=t(13),s=t(221),o=r(t(2));function r(e){return e&&e.__esModule?e:{default:e}}var c=["Account Name","Employees","Phone Number","Account Owner","Billing City"],u=["Account Name"],m=0,p=l.Row=function(e){return n.default.createElement(d.TBodyTr,{isExpanded:e.isExpanded,isSelected:e.isSelected,level:e.level,positionWithinLevel:e.positionWithinLevel,numberOfItemsAtLevel:e.numberOfItemsAtLevel,tabIndex:e.isFocusable?"0":null},!e.hasSingleRowSelection&&n.default.createElement(d.Td,{isRightAligned:!0,type:"advanced",style:{width:"3.25rem"}},n.default.createElement(d.SelectRowCell,{index:m++,checked:e.isSelected})),n.default.createElement(d.RowTh,{"data-label":"Account Name",type:"treegrid"},n.default.createElement(o.default,{"aria-hidden":"true",assistiveText:e.isExpanded?"Expand "+e.name:"Collapse "+e.name,className:(0,a.default)("slds-button_icon slds-button_icon-x-small slds-m-right_x-small",{"slds-is-disabled":null===e.isExpanded||void 0===e.isExpanded}),iconClassName:"slds-button__icon_small",symbol:"chevronright",tabIndex:"-1",title:e.isExpanded?"Collapse "+e.name:"Expand "+e.name}),n.default.createElement(d.ReadOnlyCell,{cellLink:"javascript:void(0);",cellText:e.name})),n.default.createElement(d.Td,{"data-label":"Employees",type:"treegrid"},n.default.createElement(d.ReadOnlyCell,{cellText:e.employees})),n.default.createElement(d.Td,{"data-label":"Phone Number",type:"treegrid"},n.default.createElement(d.ReadOnlyCell,{cellText:e.phone})),n.default.createElement(d.Td,{"data-label":"Account Owner",type:"treegrid"},n.default.createElement(d.ReadOnlyCell,{cellLink:"javascript:void(0);",cellText:e.owner})),n.default.createElement(d.Td,{"data-label":"Billing City",type:"treegrid"},n.default.createElement(d.ReadOnlyCell,{cellText:e.city})),n.default.createElement(d.Td,{type:"treegrid",style:{width:"3.25rem"}},n.default.createElement(d.RowActionsCell,{rowName:e.name})))};p.propTypes={city:i.default.string.isRequired,employees:i.default.string.isRequired,hasSingleRowSelection:i.default.bool,isExpanded:i.default.bool,isFocusable:i.default.bool,isSelected:i.default.bool,level:i.default.string.isRequired,name:i.default.string.isRequired,numberOfItemsAtLevel:i.default.string.isRequired,owner:i.default.string.isRequired,phone:i.default.string.isRequired,positionWithinLevel:i.default.string.isRequired};var h=l.HeadlessRow=function(e){return n.default.createElement(d.TBodyTr,{isExpanded:e.isExpanded,isSelected:e.isSelected,level:e.level,numberOfItemsAtLevel:e.numberOfItemsAtLevel,positionWithinLevel:e.positionWithinLevel,tabIndex:e.isFocusable?"0":null},!e.hasSingleRowSelection&&n.default.createElement(d.Td,{isRightAligned:!0,type:"advanced",style:{width:"3.25rem"}},n.default.createElement(d.SelectRowCell,{index:m++,checked:e.isSelected})),n.default.createElement(d.RowTh,{"data-label":"Account Name",type:"treegrid"},n.default.createElement(o.default,{"aria-hidden":"true",assistiveText:e.isExpanded?"Expand "+e.name:"Collapse "+e.name,className:(0,a.default)("slds-button_icon slds-button_icon-x-small slds-m-right_x-small",{"slds-is-disabled":null===e.isExpanded||void 0===e.isExpanded}),iconClassName:"slds-button__icon_small",symbol:"chevronright",tabIndex:"-1",title:e.isExpanded?"Collapse "+e.name:"Expand "+e.name}),n.default.createElement(d.ReadOnlyCell,{cellLink:"javascript:void(0);",cellText:e.name})),n.default.createElement(d.Td,{type:"treegrid",style:{width:"3.25rem"}},n.default.createElement(d.RowActionsCell,{rowName:e.name})))};h.displayName="HeadlessRow",h.propTypes={hasSingleRowSelection:i.default.bool,isExpanded:i.default.bool,isFocusable:i.default.bool,isSelected:i.default.bool,level:i.default.string.isRequired,name:i.default.string.isRequired,numberOfItemsAtLevel:i.default.string.isRequired,positionWithinLevel:i.default.string.isRequired};var f=l.DefaultRows=function(e){return n.default.createElement(d.TBody,null,n.default.createElement(p,{hasSingleRowSelection:e.hasSingleRowSelection,city:"Phoenix, AZ",employees:"3,100",isFocusable:!0,isSelected:!!e.hasSingleRowSelection&&null,level:"1",name:"Rewis Inc",numberOfItemsAtLevel:"4",owner:"Jane Doe",phone:"837-555-1212",positionWithinLevel:"1"}),n.default.createElement(p,{hasSingleRowSelection:e.hasSingleRowSelection,city:"San Francisco, CA",employees:"10,000",isExpanded:e.isExpanded,isSelected:e.hasSingleRowSelection?e.hasSelectedRow||null:e.hasSelectedRow||!1,level:"1",name:"Acme Corporation",numberOfItemsAtLevel:"4",owner:"John Doe",phone:"837-555-1212",positionWithinLevel:"2"}),e.additionalItem,n.default.createElement(p,{hasSingleRowSelection:e.hasSingleRowSelection,city:"New York, NY",employees:"6,000",isExpanded:!1,isSelected:!!e.hasSingleRowSelection&&null,level:"1",name:"Rohde Enterprises",numberOfItemsAtLevel:"4",owner:"John Doe",phone:"837-555-1212",positionWithinLevel:"3"}),n.default.createElement(p,{hasSingleRowSelection:e.hasSingleRowSelection,city:"Paris, France",employees:"1,234",isSelected:!!e.hasSingleRowSelection&&null,level:"1",name:"Cheese Corp",numberOfItemsAtLevel:"4",owner:"Jane Doe",phone:"837-555-1212",positionWithinLevel:"4"}))};f.displayName="DefaultRows",f.propTypes={additionalItem:i.default.node,hasSelectedRow:i.default.bool,hasSingleRowSelection:i.default.bool,isExpanded:i.default.bool};var S=l.ExpandedRow=function(e){return n.default.createElement(p,{city:"New York, NY",employees:"745",isSelected:!1,level:"2",name:"Acme Corporation (Oakland)",numberOfItemsAtLevel:"1",owner:"John Doe",phone:"837-555-1212",positionWithinLevel:"1"})},E=l.DeepNestingRows=function(e){return n.default.createElement(d.TBody,null,n.default.createElement(p,{level:"1",positionWithinLevel:"1",numberOfItemsAtLevel:"4",name:"Rewis Inc",employees:"3,100",phone:"837-555-1212",owner:"Jane Doe",city:"Phoenix, AZ",isFocusable:!0,isSelected:!1}),n.default.createElement(p,{isExpanded:!0,level:"1",positionWithinLevel:"2",numberOfItemsAtLevel:"4",name:"Acme Corporation",employees:"10,000",phone:"837-555-1212",owner:"John Doe",city:"San Francisco, CA",isSelected:!1}),n.default.createElement(p,{isExpanded:!0,level:"2",positionWithinLevel:"1",numberOfItemsAtLevel:"2",name:"Acme Corporation (Bay Area)",employees:"3,000",phone:"837-555-1212",owner:"John Doe",city:"New York, NY",isSelected:!1}),n.default.createElement(p,{level:"3",positionWithinLevel:"1",numberOfItemsAtLevel:"2",name:"Acme Corporation (Oakland)",employees:"745",phone:"837-555-1212",owner:"John Doe",city:"New York, NY",isSelected:!1}),n.default.createElement(p,{level:"3",positionWithinLevel:"2",numberOfItemsAtLevel:"2",name:"Acme Corporation (San Francisco)",employees:"578",phone:"837-555-1212",owner:"Jane Doe",city:"Los Angeles, CA",isSelected:!1}),n.default.createElement(p,{isExpanded:!0,level:"2",positionWithinLevel:"2",numberOfItemsAtLevel:"2",name:"Acme Corporation (East)",employees:"430",phone:"837-555-1212",owner:"John Doe",city:"San Francisco, CA",isSelected:!1}),n.default.createElement(p,{level:"3",positionWithinLevel:"1",numberOfItemsAtLevel:"2",name:"Acme Corporation (NY)",employees:"1,210",phone:"837-555-1212",owner:"Jane Doe",city:"New York, NY",isSelected:!1}),n.default.createElement(p,{isExpanded:!0,level:"3",positionWithinLevel:"2",numberOfItemsAtLevel:"2",name:"Acme Corporation (VA)",employees:"410",phone:"837-555-1212",owner:"John Doe",city:"New York, NY",isSelected:!1}),n.default.createElement(p,{isExpanded:!0,level:"4",positionWithinLevel:"1",numberOfItemsAtLevel:"1",name:"Allied Technologies",employees:"390",phone:"837-555-1212",owner:"Jane Doe",city:"Los Angeles, CA",isSelected:!1}),n.default.createElement(p,{level:"5",positionWithinLevel:"1",numberOfItemsAtLevel:"1",name:"Allied Technologies (UV)",employees:"270",phone:"837-555-1212",owner:"John Doe",city:"San Francisco, CA",isSelected:!1}),n.default.createElement(p,{isExpanded:!0,level:"1",positionWithinLevel:"3",numberOfItemsAtLevel:"4",name:"Rohde Enterprises",employees:"6,000",phone:"837-555-1212",owner:"John Doe",city:"New York, NY",isSelected:!1}),n.default.createElement(p,{level:"2",positionWithinLevel:"1",numberOfItemsAtLevel:"1",name:"Rohde Enterprises (UCA)",employees:"2,540",phone:"837-555-1212",owner:"John Doe",city:"New York, NY",isSelected:!1}),n.default.createElement(p,{isExpanded:!0,level:"1",positionWithinLevel:"4",numberOfItemsAtLevel:"4",name:"Tech Labs",employees:"1,856",phone:"837-555-1212",owner:"John Doe",city:"New York, NY",isSelected:!1}),n.default.createElement(p,{level:"2",positionWithinLevel:"1",numberOfItemsAtLevel:"1",name:"Opportunity Resources Inc",employees:"1,934",phone:"837-555-1212",owner:"John Doe",city:"Los Angeles, CA",isSelected:!1}))},w=l.HeadlessRows=function(e){return n.default.createElement(d.TBody,null,n.default.createElement(h,{hasSingleRowSelection:e.hasSingleRowSelection,isFocusable:!0,isSelected:!!e.hasSingleRowSelection&&null,level:"1",name:"Rewis Inc",numberOfItemsAtLevel:"4",positionWithinLevel:"1"}),n.default.createElement(h,{hasSingleRowSelection:e.hasSingleRowSelection,isExpanded:e.isExpanded,isSelected:e.hasSingleRowSelection?e.hasSelectedRow||null:e.hasSelectedRow||!1,level:"1",name:"Acme Corporation",numberOfItemsAtLevel:"4",positionWithinLevel:"2"}),n.default.createElement(h,{hasSingleRowSelection:e.hasSingleRowSelection,isExpanded:!1,isSelected:!!e.hasSingleRowSelection&&null,level:"1",name:"Rohde Enterprises",numberOfItemsAtLevel:"4",positionWithinLevel:"3"}),n.default.createElement(h,{hasSingleRowSelection:e.hasSingleRowSelection,isSelected:!!e.hasSingleRowSelection&&null,level:"1",name:"Cheese Corp",numberOfItemsAtLevel:"4",positionWithinLevel:"4"}))};w.displayName="HeadlessRows",w.propTypes={isExpanded:i.default.any,hasSelectedRow:i.default.bool,hasSingleRowSelection:i.default.bool},l.default=n.default.createElement(s.TreeGrid,{isBordered:!0,isFixedLayout:!0,isResizable:!0,selectionType:"multiple"},n.default.createElement(d.AdvancedDataTableHead,{columns:c,hasMenus:!0}),n.default.createElement(f,{isExpanded:!1}));l.states=[{id:"expanded",label:"Expanded",element:n.default.createElement(s.TreeGrid,{isBordered:!0,isFixedLayout:!0,isResizable:!0,selectionType:"multiple"},n.default.createElement(d.AdvancedDataTableHead,{columns:c,hasMenus:!0}),n.default.createElement(f,{isExpanded:!0,additionalItem:n.default.createElement(S,null)}))},{id:"selected-row",label:"Selected row",element:n.default.createElement(s.TreeGrid,{isBordered:!0,isFixedLayout:!0,isResizable:!0,selectionType:"multiple"},n.default.createElement(d.AdvancedDataTableHead,{columns:c,hasMenus:!0}),n.default.createElement(f,{isExpanded:!0,hasSelectedRow:!0,additionalItem:n.default.createElement(S,null)}))},{id:"deep-nesting",label:"Deeply nested branches",element:n.default.createElement(s.TreeGrid,{isBordered:!0,isFixedLayout:!0,isResizable:!0,selectionType:"multiple"},n.default.createElement(d.AdvancedDataTableHead,{columns:c,hasMenus:!0}),n.default.createElement(E,null))}],l.examples=[{id:"treegrid-headless",label:"Headless",element:n.default.createElement(s.TreeGrid,{isBordered:!0,selectionType:"multiple",hasHiddenHeader:!0},n.default.createElement(d.AdvancedDataTableHead,{columns:u,hasSingleRowSelect:!0,isHidden:!0}),n.default.createElement(w,{isExpanded:!1}))},{id:"treegrid-headless-selected-row",label:"Headless with selected row",element:n.default.createElement(s.TreeGrid,{isBordered:!0,selectionType:"multiple",hasHiddenHeader:!0},n.default.createElement(d.AdvancedDataTableHead,{columns:u,hasSingleRowSelect:!0,isHidden:!0}),n.default.createElement(w,{isExpanded:!1,hasSelectedRow:!0}))},{id:"treegrid-headless-no-borders",label:"Headless with no borders",element:n.default.createElement(s.TreeGrid,{selectionType:"multiple",hasHiddenHeader:!0},n.default.createElement(d.AdvancedDataTableHead,{hasSingleRowSelect:!0,columns:u,isHidden:!0}),n.default.createElement(w,{isExpanded:!1}))},{id:"treegrid-headless-no-borders-selected-row",label:"Headless with no borders and a selected row",element:n.default.createElement(s.TreeGrid,{selectionType:"multiple",hasHiddenHeader:!0},n.default.createElement(d.AdvancedDataTableHead,{hasSingleRowSelect:!0,columns:u,isHidden:!0}),n.default.createElement(w,{isExpanded:!1,hasSelectedRow:!0}))},{id:"treegrid-single-select",label:"Single select",element:n.default.createElement(s.TreeGrid,{isBordered:!0,isFixedLayout:!0,isResizable:!0},n.default.createElement(d.AdvancedDataTableHead,{hasNoRowSelection:!0,columns:c,hasMenus:!0}),n.default.createElement(f,{isExpanded:!1,hasSingleRowSelection:!0}))},{id:"treegrid-single-select-selected-row",label:"Single select with a selected row",element:n.default.createElement(s.TreeGrid,{isBordered:!0,isFixedLayout:!0,isResizable:!0},n.default.createElement(d.AdvancedDataTableHead,{hasNoRowSelection:!0,columns:c,hasMenus:!0}),n.default.createElement(f,{isExpanded:!1,hasSelectedRow:!0,hasSingleRowSelection:!0}))},{id:"treegrid-single-select-headless",label:"Single select headless",element:n.default.createElement(s.TreeGrid,{isBordered:!0,hasHiddenHeader:!0},n.default.createElement(d.AdvancedDataTableHead,{hasNoRowSelection:!0,columns:u,isHidden:!0}),n.default.createElement(w,{isExpanded:!1,hasSingleRowSelection:!0}))},{id:"treegrid-single-select-headless-selected",label:"Single select headless with selected row",element:n.default.createElement(s.TreeGrid,{isBordered:!0,hasHiddenHeader:!0},n.default.createElement(d.AdvancedDataTableHead,{hasNoRowSelection:!0,columns:u,isHidden:!0}),n.default.createElement(w,{isExpanded:!1,hasSelectedRow:!0,hasSingleRowSelection:!0}))},{id:"treegrid-single-select-headless-no-borders",label:"Single select headless with no borders",element:n.default.createElement(s.TreeGrid,{hasHiddenHeader:!0},n.default.createElement(d.AdvancedDataTableHead,{hasNoRowSelection:!0,columns:u,isHidden:!0}),n.default.createElement(w,{isExpanded:!1,hasSingleRowSelection:!0}))},{id:"treegrid-single-select-headless-no-borders-with-selected",label:"Single select headless with no borders and a selected row",element:n.default.createElement(s.TreeGrid,{hasHiddenHeader:!0},n.default.createElement(d.AdvancedDataTableHead,{hasNoRowSelection:!0,columns:u,isHidden:!0}),n.default.createElement(w,{isExpanded:!1,hasSelectedRow:!0,hasSingleRowSelection:!0}))}]}});