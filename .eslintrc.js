export default {
  root: true,
  env: {
    node: true,
    browser: true,
    es2022: true,
  },
  extends: ["plugin:vue/vue3-recommended", "eslint:recommended", "prettier"],
  parserOptions: {
    parser: "@babel/eslint-parser",
    ecmaVersion: 2022,
    sourceType: "module",
    requireConfigFile: false,
    babelOptions: {
      plugins: ["@babel/plugin-syntax-import-assertions"],
    },
  },
  rules: {
    indent: ["error", 2],
    "vue/html-indent": ["error", 2],
    "vue/script-indent": ["error", 2],
    "vue/multi-word-component-names": "off", // Optional: disable if you don't follow this convention
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
  },
};
