Blog.directive('timeAgo', function ($timeout) {
    return {
        restrict: 'A',
        scope: {
            title: '@'
        },
        link: function (scope, elem, attrs) {
            var updateTime = function () {
                if (attrs.title) {
                    elem.text(moment(attrs.title).fromNow());
                    $timeout(updateTime, 15000);
                }
            };
            scope.$watch(attrs.title, updateTime);
        }
    };
});
// Formats a date as the time since creation

Blog.directive('pendingBar', ['$rootScope',
    function ($rootScope) {
        return {
            link: function (scope, element, attrs) {
                element.addClass('hide');
                $rootScope.$on('$routeChangeStart', function () {
                    element.removeClass('hide');
                });
                $rootScope.$on('$routeChangeSuccess', function () {
                    element.addClass('hide');
                });
                $rootScope.$on('$routeChangeError', function () {
                    element.removeClass('hide');
                });
            }
        };
    }]);
// Pending bar shows when the user tries to switch to another view.

Blog.directive('viewState', ['$rootScope',
    function ($rootScope) {
        return {
            link: function (scope, element, attrs) {
                element.addClass('hide');
                $rootScope.$on('$routeChangeStart', function () {
                    element.addClass('hide');
                });
                $rootScope.$on('$routeChangeSuccess', function () {
                    element.removeClass('hide');
                });
                $rootScope.$on('$routeChangeError', function () {
                    element.addClass('hide');
                });
            }
        };
// Hides the view until the routing has completed.
    }]);