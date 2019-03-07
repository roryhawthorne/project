import Home from "views/Home/Home.jsx";
import MyBuddy from "views/myBuddy/myBuddy.jsx";
import UserPage from "views/UserPage/UserPage.jsx";
import FAQ from "views/FAQ/FAQ.jsx";
import Admin from "views/Admin/Admin.jsx";
import SuperAdmin from "views/SuperAdmin/SuperAdmin.jsx";
import RegisterForm from "views/RegisterForm/RegisterForm.jsx";

var dashRoutes = [
  {
    path: "/home",
    name: "Home",
    component: Home
  },
  {
    path: "/myBuddy",
    name: "My Buddy",
    component: MyBuddy
  },
  {
    path: "/user-page",
    name: "User Profile",
    component: UserPage
  },
  {
    path: "/faq",
    name: "FAQs",
    component: FAQ
  },
  {
    path: "/admin",
    name: "Admin",
    component: Admin
  },
  {
    path: "/super-admin",
    name: "Super Admin",
    component: SuperAdmin
  },
  {
    path: "/RegisterForm",
    name: "redirect form after sign up confirmation",
    component: RegisterForm
  },

  { redirect: true, path: "/", pathTo: "/home", name: "Home" }
];
export default dashRoutes;
