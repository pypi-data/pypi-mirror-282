import { i as a } from "./init-f9637058.js";
class o extends Map {
  constructor(n, t = g) {
    if (super(), Object.defineProperties(this, { _intern: { value: /* @__PURE__ */ new Map() }, _key: { value: t } }), n != null)
      for (const [r, s] of n)
        this.set(r, s);
  }
  get(n) {
    return super.get(c(this, n));
  }
  has(n) {
    return super.has(c(this, n));
  }
  set(n, t) {
    return super.set(l(this, n), t);
  }
  delete(n) {
    return super.delete(p(this, n));
  }
}
function c({ _intern: e, _key: n }, t) {
  const r = n(t);
  return e.has(r) ? e.get(r) : t;
}
function l({ _intern: e, _key: n }, t) {
  const r = n(t);
  return e.has(r) ? e.get(r) : (e.set(r, t), t);
}
function p({ _intern: e, _key: n }, t) {
  const r = n(t);
  return e.has(r) && (t = e.get(r), e.delete(r)), t;
}
function g(e) {
  return e !== null && typeof e == "object" ? e.valueOf() : e;
}
const f = Symbol("implicit");
function h() {
  var e = new o(), n = [], t = [], r = f;
  function s(u) {
    let i = e.get(u);
    if (i === void 0) {
      if (r !== f)
        return r;
      e.set(u, i = n.push(u) - 1);
    }
    return t[i % t.length];
  }
  return s.domain = function(u) {
    if (!arguments.length)
      return n.slice();
    n = [], e = new o();
    for (const i of u)
      e.has(i) || e.set(i, n.push(i) - 1);
    return s;
  }, s.range = function(u) {
    return arguments.length ? (t = Array.from(u), s) : t.slice();
  }, s.unknown = function(u) {
    return arguments.length ? (r = u, s) : r;
  }, s.copy = function() {
    return h(n, t).unknown(r);
  }, a.apply(s, arguments), s;
}
export {
  h as o
};
