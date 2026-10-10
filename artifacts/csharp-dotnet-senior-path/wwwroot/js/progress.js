window.learningProgress = {
    key: "trilha-csharp-dotnet-senior-progress",
    load: function () {
        return window.localStorage.getItem(this.key) || "";
    },
    save: function (value) {
        window.localStorage.setItem(this.key, value || "");
    }
};
