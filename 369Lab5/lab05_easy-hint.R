myfit <- function(train_df, test_df, a=0){
  # Note: lasso a = 1; ridge: a = 0

  # separate Xs and Y
  train_X <- as.matrix(train_df[,-1])
  train_y <- train_df$Y
  test_X <- as.matrix(test_df[,-1])
  test_y <- test_df$Y

  # cross validate with glmnet(..., alpha = a)
  cv.fit <- cv.glmnet(train_X, train_y, alpha = a,
                      lambda = lambdas)
  plot(cv.fit)

  # optimal model
  opt.l <- cv.fit$lambda.min
  opt.fit <- cv.fit$glmnet.fit
  betas <- as.matrix(coef(opt.fit, s = cv.fit$lambda.min))
  n_non0_betas <- sum(betas != 0)

  # predict on test_df and calculate our stats
  pred_y <- predict(opt.fit, s = opt.l, newx = test_X)
  mse <- mean((test_y - pred_y)^2)

  return(list(alpha = a,
              mse = mse,
              opt.lambda = opt.l,
              n_non0_betas = n_non0_betas
              ))

}
